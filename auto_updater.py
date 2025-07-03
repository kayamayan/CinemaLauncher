import os, requests, tempfile, shutil, subprocess, sys
from pathlib import Path
from packaging import version
import token

OWNER, REPO = "kayamayan", "CinemaLauncher"
API_LATEST  = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
TOKEN       = token.PAT          # PAT, scope: repo
HDR_API     = {"Authorization": f"token {TOKEN}"}         # JSON
HDR_BIN     = {"Authorization": f"token {TOKEN}",
               "Accept": "application/octet-stream"}      # ▶ binary

def latest_asset_api_url():
    j = requests.get(API_LATEST, headers=HDR_API, timeout=10).json()
    tag = j["tag_name"].lstrip("v")
    asset_api = next(a["url"]                       # ← ‘url’, NOT browser_download_url
                     for a in j["assets"]
                     if a["name"].endswith(".exe"))
    return tag, asset_api

def download_private(asset_api_url: str, dest: Path):
    with requests.get(asset_api_url, headers=HDR_BIN,
                      stream=True, timeout=30) as r:
        r.raise_for_status()                        # 200 (이미 바이너리)
        with open(dest, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    if dest.stat().st_size < 1_000_000:             # 1 MB 미만 → 오류 페이지
        raise RuntimeError("downloaded file too small – check token / url")

def swap_and_restart(new_exe: Path):
    old = Path(sys.executable)
    bak = old.with_suffix(".bak")
    if bak.exists():
        bak.unlink()
    old.replace(bak)
    new_exe.replace(old)                 # WinError 17 없음 (같은 폴더)

    # ── ❶ _MEI, PYTHONHOME, PYTHONPATH 제거 ──
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(('_MEI', 'PYTHONHOME', 'PYTHONPATH'))}
    # ── ❷ PATH 맨 앞에 exe 폴더 추가 (python311.dll 탐색) ──
    env["PATH"] = f"{old.parent};{env.get('PATH', '')}"

    subprocess.Popen([str(old)], env=env, close_fds=True)
    sys.exit()


def check_for_updates(cur_ver="1.0.0"):
    tag, api_url = latest_asset_api_url()
    if version.parse(tag) <= version.parse(cur_ver):
        return
    old = Path(sys.executable)
    tmp = old.with_suffix(".new")
    download_private(api_url, tmp)
    swap_and_restart(tmp)
