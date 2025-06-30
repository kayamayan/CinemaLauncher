# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('./ui', './ui'),
		   ('./config.py', './'),
		   ('./database.py', './'),
		   ('./perforce.py', './'),
		   ('./settings.py', './'),
		   ('./uiStyle.py', './'),
		   ('./commands.py', './'),
		   ('./user.py', './'),
		   ('./version.py', './'),
		   ('./projectManager.py', './')],
    hiddenimports=['requests',
                   'P4',
				   'pymongo',
				   'json',
				   'win32api'],
    hookspath=['F:\\gitRepos\\CinemaLauncher\\venv\\Lib\\site-packages\\pyupdater\\hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CinemaLauncher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='F:/cinema_tools/apps/CinemaLauncher/vt_logo_inverse.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
