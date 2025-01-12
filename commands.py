import os
import subprocess

from database import VtDatabaseWeb

CURRENT_DIR = os.path.dirname(__file__).replace("\\", '/')


class Commands:
    def __init__(self):
        self.db = VtDatabaseWeb()

    def launch(self, engine, project, raytracing):
        subprocess.Popen([engine, project, raytracing], stdin=None, stdout=None, stderr=None, close_fds=True)

    def sync(self, paths):
        for path in paths:
            os.system(f"start /wait cmd /c p4 sync {path}/...")
            # p = subprocess.Popen(["p4", "sync", f"{path}/..."], shell=True)
            # p.wait()

    @staticmethod
    def open_contents(directory):
        directory = directory.replace("/", "\\")
        subprocess.Popen(fr'explorer "{directory}"')

    @staticmethod
    def open_resource(directory):
        directory = directory.replace("/", "\\")
        subprocess.Popen(fr'explorer "{directory}"')

    def save_project(self, data: dict):
        return self.db.update_project_db(data)

    def delete_project(self, data: dict):
        return self.db.update_project_db(data)
