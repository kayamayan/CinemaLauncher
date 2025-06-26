import os
import json
import logging
import subprocess

CONFIG_FILE = os.environ["APPDATA"].replace("\\", "/") + "/CinemaStudio/CinemaLauncher/config/CinemaLauncher.json"

CONFIG = {
    "Project": None,
    "CurrentTab": None,
    "Settings": {
        "EngineRoot": None,
        "EnableDx12": False,
        "P4exe": r"C:\Program Files\Perforce\p4v.exe",
        "SyncResource": True,
        "ForceSync": False,
        "ExceptDDC": True,
        "ExceptIntermediate": True,
        "ExceptSaved": True,
        "IncludeFACS": True
    }
}

SYNC_PATHS = {
    "SyncResource": "{resource_path}",
    "ExceptDDC": "{content_path}/DerivedDataCache",
    "ExceptIntermediate": "{content_path}/Intermediate",
    "ExceptSaved": "{content_path}/Saved"
}

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def init_config():
    config_path = "/".join(CONFIG_FILE.split("/")[:-1])
    if not os.path.exists(config_path):
        os.makedirs(config_path)


def write_json(data, filepath):
    with open(filepath, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        file.close()
    # with open(filepath, 'w') as f:
    #     json.dump(data, f, indent=4)
    #     f.close()


def read_json(filepath):
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data


def open_chrome(url):
    p = subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", '--kiosk', url])
    p.wait()


def get_config():
    """Return CONFIG if CONFIG_FILE not exists

    Returns: harvester configuration json data
    """
    if os.path.exists(CONFIG_FILE):
        data = read_json(CONFIG_FILE)
    else:
        init_config()
        set_config(CONFIG)
        data = CONFIG
    return data


def set_config(data):
    init_config()
    write_json(data, CONFIG_FILE)
    logger.debug(u'{0}'.format(CONFIG_FILE))
