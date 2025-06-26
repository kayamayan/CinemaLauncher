# encoding:utf-8
"""

"""
import time
import os
import winreg
import socket
import traceback

import win32api
# from win10toast_click import ToastNotifier
from PySide6 import QtWidgets, QtCore, QtGui

from ui import mainWindow
from database import CinemaDatabase#VtDatabaseWeb
import settings
import config
import perforce
from commands import Commands
import version

# import update

CURRENT_DIR = os.path.dirname(__file__).replace("\\", '/')
RESOURCE_DIR = CURRENT_DIR + "/ui/resource"

os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'


class UpdateCheckThread(QtCore.QThread):
    update_que = QtCore.Signal(bool)
    version = None

    def __init__(self):
        QtCore.QThread.__init__(self)
        # self.working = True

    def __del__(self):
        self.wait()

    def run(self):
        delay = 60
        next_time = time.time()
        while True:
            time.sleep(max(0, next_time - time.time()))
            try:
                import importlib.util
                spec = importlib.util.spec_from_file_location("module.name",
                                                              r"\\cinemaserver\Tcinema\VTLIB\apps\VtLauncher\version.py")
                version_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(version_module)
                major, minor, patch = version_module.version_info
                # major, minor, patch = (2, 0, 0)
                self.version = version_module.version
                cur_major, cur_minor, cur_patch = version.version_info
                if major > cur_major:
                    self.update_que.emit(True)
                elif major == cur_major and minor > cur_minor:
                    self.update_que.emit(True)
                elif major == cur_major and minor == cur_minor and patch > cur_patch:
                    self.update_que.emit(True)
            except Exception:
                traceback.print_exc()
                # in production code you might want to have this instead of course:
                # logger.exception("Problem while executing repetitive task.")
            # skip tasks if we are behind schedule:
            next_time += (time.time() - next_time) // delay * delay + delay

    def stop(self):
        self.terminate()
        # self.working = False
        # self.quit()
        # self.wait()


class MainWindow(mainWindow.Window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        # self._toaster = ToastNotifier()
        self._update_message_box = None
        self._update_check_thread = None
        self._db = None
        self.config = None
        self.commands = None
        self.update_cls = None
        self.p4cmd = None
        self.drag_pos = None

        self.setWindowTitle(f"Cinema Apps {version.version}")

        icon = QtGui.QIcon(RESOURCE_DIR + "/icons/vt_logo_30.png")
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)
        self.tray_icon.show()
        self.tray_icon.setToolTip("Cinema Launcher")
        self.tray_icon.activated.connect(self.icon_activated)

        self.open_action = QtGui.QAction("Open")
        self.quit_action = QtGui.QAction("Quit")
        self.open_action.triggered.connect(self.show)
        self.quit_action.triggered.connect(QtWidgets.QApplication.quit)

        self.tray_icon_menu = QtWidgets.QMenu(self)
        self.tray_icon_menu.addAction(self.open_action)
        self.tray_icon_menu.addSeparator()
        self.tray_icon_menu.addAction(self.quit_action)

        # Add the menu to the tray
        self.tray_icon.setContextMenu(self.tray_icon_menu)

    def setup_ui(self):
        # self._update_check_thread = UpdateCheckThread()

        # self.tray_icon = None
        self._db = CinemaDatabase()
        self.project_manager.db = self._db
        self.config = config.get_config()
        self.commands = Commands()
        self.p4cmd = perforce.P4Cmd()
        # self.create_tray_icon()

        self.connect_signals()
        self.connect_btn_signals()

        self.update_projects()

        self.set_ui()

        self.installEventFilter(self)
        self.tab_index_changed()

        # self._update_check_thread.start()

    def create_tray_icon(self):
        # Create the icon
        icon = QtGui.QIcon(RESOURCE_DIR + "/icons/vt_logo_30.png")

        # Create the tray
        self.tray_icon.setIcon(icon)
        # self.tray_icon.setVisible(True)

        if self.tray_icon.isSystemTrayAvailable():
            # self.tray_icon.setIcon(self.windowIcon())
            # Create the menu
            open_action = QtGui.QAction("Open")
            quit_action = QtGui.QAction("Quit")
            open_action.triggered.connect(self.show)
            quit_action.triggered.connect(QtWidgets.QApplication.quit)

            self.tray_icon_menu.addAction(open_action)
            self.tray_icon_menu.addSeparator()
            self.tray_icon_menu.addAction(quit_action)

            # Add the menu to the tray
            self.tray_icon.setContextMenu(self.tray_icon_menu)
            self.tray_icon.activated.connect(self.icon_activated)

            self.tray_icon.show()
        else:
            # Destroy unused var
            self.tray_icon = None

    def icon_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.setVisible(True)
            # self.show()

    def check_permission(self):
        ip_address = socket.gethostbyname(socket.gethostname())
        if ip_address not in settings.VtLauncherSettings.ADMINS:
            self.project_manager.setHidden(True)
            self.tab_project_manager_button.setHidden(True)

    @property
    def content_dir(self):
        project = self.vtLauncher_widget.combobox_projects.currentText().rsplit(" (", 1)[0]
        project_data = self._db.get_project_data(project)
        path = project_data["content_path"].replace("//", self.p4cmd.get_workspace()["depot"] + "/")
        # print(path)
        return path

    @property
    def resource_dir(self):
        project = self.vtLauncher_widget.combobox_projects.currentText().rsplit(" (", 1)[0]
        project_data = self._db.get_project_data(project)
        path = project_data["resource_path"].replace("//", self.p4cmd.get_workspace()["resource"] + "/")
        # print(path)
        return path

    def connect_signals(self):
        self.stacked_widget.currentChanged.connect(self.tab_index_changed)
        # self._update_check_thread.update_que.connect(self.update_app)

    def connect_btn_signals(self):
        self.btn_close.clicked.connect(self.close_ui)
        self.tab_vtlauncher_button.clicked.connect(self.tab_change)
        self.tab_project_manager_button.clicked.connect(self.tab_change)
        self.vtLauncher_widget.btn_refersh_project.clicked.connect(self.update_projects)
        self.vtLauncher_widget.show_finished_checkbox.stateChanged.connect(self.update_projects)
        self.project_manager.btn_refersh_project.clicked.connect(self.update_projects)
        self.project_manager.show_finished_checkbox.stateChanged.connect(self.update_projects)
        self.settings_button.clicked.connect(self.tab_change)
        self.vtLauncher_widget.btn_sync_launch.clicked.connect(self.doit)
        self.vtLauncher_widget.btn_sync.clicked.connect(self.doit)
        self.vtLauncher_widget.btn_launch.clicked.connect(self.doit)
        self.vtLauncher_widget.btn_open_content.clicked.connect(lambda x: Commands.open_contents(self.content_dir))
        self.vtLauncher_widget.btn_open_resource.clicked.connect(lambda x: Commands.open_resource(self.resource_dir))

    def update_clicked(self):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = CURRENT_DIR

        win32api.ShellExecute(0, None,
                              '\\\\cinemaserver\\Tcinema\\VTLIB\\global\\Python39\\python.exe',
                              fr"{application_path}\update.py",
                              None, 1)
        self.close_ui()

    @QtCore.Slot(bool)
    def update_app(self, que):
        if self._update_message_box:
            self._update_message_box.close()
        if que:
            # self._toaster.show_toast(
            #     "VtLauncher 새로운 버전이 있습니다.",
            #     "클릭하면 업데이트를 진행합니다.",
            #     icon_path=None,  # 'icon_path'
            #     duration=5,
            #     # for how many seconds toast should be visible; None = leave notification in Notification Center
            #     threaded=True,
            #     # True = run other code in parallel; False = code execution will wait till notification disappears
            #     callback_on_click=self.update_clicked
            # )
            self._update_message_box = QtWidgets.QMessageBox()
            self._update_message_box.setWindowTitle("Software Update")
            self._update_message_box.setText("A new version of VtLauncher is available.\nWould you like to update?")
            self._update_message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            self._update_message_box.setDefaultButton(QtWidgets.QMessageBox.Yes)
            message = self._update_message_box.exec_()

            if message == QtWidgets.QMessageBox.Yes:
                if getattr(sys, 'frozen', False):
                    application_path = os.path.dirname(sys.executable)
                else:
                    application_path = CURRENT_DIR

                win32api.ShellExecute(0, None,
                                      '\\\\cinemaserver\\Tcinema\\VTLIB\\global\\Python39\\python.exe',
                                      fr"{application_path}\update.py",
                                      None, 1)
                self.close_ui()

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.drag_pos = event.globalPos()

    def close_ui(self):
        self.close()
        QtCore.QCoreApplication.instance().quit()

    def closeEvent(self, event):
        event.ignore()
        self._hide_main_window()
        self.save_settings()

    def _hide_main_window(self, _=''):
        self.setVisible(False)

    @property
    def settings(self):
        settings_data = self.settings_widget.get_settings()
        return settings_data

    def select_menu(self, get_style):
        select = get_style + settings.VtLauncherSettings.MENU_SELECTED_STYLESHEET
        return select

    def deselect_menu(self, get_style):
        deselect = get_style.replace(settings.VtLauncherSettings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def reset_style(self, widget):
        for w in self.frame_left_menu.findChildren(QtWidgets.QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselect_menu(w.styleSheet()))

    def set_ui(self):
        self.vtLauncher_widget.combobox_projects.setCurrentText(str(self.config["Project"]))
        if self.config["CurrentTab"]:
            self.stacked_widget.setCurrentIndex(self.config["CurrentTab"])
        self.vtLauncher_widget.show_finished_checkbox.setChecked(self.config.get("ShowFinished_VTL", False))
        self.project_manager.show_finished_checkbox.setChecked(self.config.get("ShowFinished_PRM", False))
        if not self.config["Settings"]["EngineRoot"]:
            self.config["Settings"]["EngineRoot"] = self.get_engine_path("4.27")
        # self.project_manager.update_project_info()
        self.settings_widget.set_ui(self.config)
        # self.check_permission()

    def save_settings(self):
        self.config["Project"] = str(self.vtLauncher_widget.combobox_projects.currentText())
        self.config["CurrentTab"] = self.stacked_widget.currentIndex()
        self.config["ShowFinished_VTL"] = self.vtLauncher_widget.show_finished_checkbox.isChecked()
        self.config["ShowFinished_PRM"] = self.project_manager.show_finished_checkbox.isChecked()
        self.config["Settings"] = self.settings_widget.get_settings()
        config.set_config(self.config)
        print("Settings Saved")

    def get_engine_path(self, engine_version):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, fr"SOFTWARE\EpicGames\Unreal Engine\{engine_version}")
            value = os.path.dirname(winreg.QueryValueEx(key, "InstalledDirectory")[0])
        except FileNotFoundError as e:
            value = r"C:\Program Files\Epic Games"
        return value

    def tab_change(self):
        sending_button = self.sender()

        if sending_button.objectName() == "tab_vtlauncher_button":
            self.stacked_widget.setCurrentWidget(self.vtLauncher_widget)
            self.reset_style(self.tab_vtlauncher_button.objectName())
            self.tab_vtlauncher_button.setStyleSheet(self.select_menu(self.tab_vtlauncher_button.styleSheet()))
        elif sending_button.objectName() == "tab_project_manager_button":
            self.stacked_widget.setCurrentWidget(self.project_manager)
            self.reset_style(self.tab_project_manager_button.objectName())
            self.tab_project_manager_button.setStyleSheet(
                self.select_menu(self.tab_project_manager_button.styleSheet())
            )
        elif sending_button.objectName() == "settings_button":
            self.stacked_widget.setCurrentWidget(self.settings_widget)
            self.reset_style(self.settings_button.objectName())
            self.settings_button.setStyleSheet(
                self.select_menu(self.settings_button.styleSheet())
            )

    def tab_index_changed(self):
        if self.stacked_widget.currentIndex() == 0:
            self.stacked_widget.setCurrentWidget(self.vtLauncher_widget)
            self.reset_style(self.tab_vtlauncher_button.objectName())
            self.tab_vtlauncher_button.setStyleSheet(self.select_menu(self.tab_vtlauncher_button.styleSheet()))
        elif self.stacked_widget.currentIndex() == 1:
            self.stacked_widget.setCurrentWidget(self.project_manager)
            self.reset_style(self.tab_project_manager_button.objectName())
            self.tab_project_manager_button.setStyleSheet(
                self.select_menu(self.tab_project_manager_button.styleSheet())
            )
        elif self.stacked_widget.currentIndex() == 2:
            self.stacked_widget.setCurrentWidget(self.settings_widget)
            self.reset_style(self.settings_button.objectName())
            self.settings_button.setStyleSheet(
                self.select_menu(self.settings_button.styleSheet())
            )

    def update_projects(self):
        include_finished_vtl = self.vtLauncher_widget.show_finished_checkbox.isChecked()
        projects = self._db.get_projects(include_finished_vtl)
        if projects:
            # model = QtGui.QStandardItemModel(0, 1)
            # for project_name, object_id in projects.items():
            #     item = QtGui.QStandardItem(project_name)
            #     # item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            #     # item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
            #     item.setData(object_id, QtCore.Qt.UserRole)
            #     model.appendRow(item)
            # self.vtLauncher_widget.combobox_projects.setModel(model)
            # self.project_manager.combobox_projects.setModel(model)
            self.vtLauncher_widget.combobox_projects.clear()
            self.vtLauncher_widget.combobox_projects.addItems(projects)

        include_finished_prm = self.project_manager.show_finished_checkbox.isChecked()
        projects = self._db.get_projects(include_finished_prm)
        if projects:
            self.project_manager.combobox_projects.clear()
            self.project_manager.combobox_projects.addItems(projects)

    def doit(self):
        sender = self.sender()
        project = self.vtLauncher_widget.combobox_projects.currentText().rsplit(" (", 1)[0]
        project_data = self._db.get_project_data(project)
        # resource_path = project_data["resource_path"].replace("//Resource", self.p4cmd.get_workspace()["Resource"])
        # content_path = project_data["content_path"].replace("//depot", self.p4cmd.get_workspace()["depot"])
        ue_exe_file = "UnrealEditor.exe" if project_data["engine_version"].startswith("UE_5") else "UE4Editor.exe"
        engine = "/".join([self.settings["EngineRoot"].replace("\\", "/"),
                           project_data["engine_version"],
                           "Engine/Binaries/Win64",
                           ue_exe_file])
        project_file = "/".join([self.content_dir, project_data["name"] + ".uproject"])
        enable_dx12 = "-dx12" if self.settings["EnableDx12"] else ""
        sync_paths = [project_data["content_path"]]

        if sender == self.vtLauncher_widget.btn_sync_launch or sender == self.vtLauncher_widget.btn_sync:
            keys = ["ExceptDDC", "ExceptIntermediate", "ExceptSaved"]
            if self.settings["SyncResource"]:
                sync_paths.append(project_data["resource_path"])
            if self.settings["IncludeFACS"]:
                sync_paths.append('"//Resource/TeamData/CharacterSetup/FACS_Rig_R&D"')
            for k in keys:
                if not self.settings[k]:
                    sync_paths.append(config.SYNC_PATHS[k].format(content_path=project_data["content_path"]))
            self.commands.sync(sync_paths)
            # for path in sync_paths:
            #     self.p4cmd.pull(path)
            if sender == self.vtLauncher_widget.btn_sync_launch:
                self.commands.launch(engine=engine, project=project_file, raytracing=enable_dx12)
        elif sender == self.vtLauncher_widget.btn_launch:
            # print(project_file)
            self.commands.launch(engine, project_file, enable_dx12)


if __name__ == "__main__":
    import sys

    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    app.setQuitOnLastWindowClosed(False)

    lock_file = QtCore.QLockFile(QtCore.QDir.tempPath() + "/vtlauncher.lock")

    try:
        if lock_file.tryLock(0):
            vt_launcher_ui = MainWindow()

            # splash_pix = QtGui.QPixmap(RESOURCE_DIR + "/VT_Logo.png")

            # splash = QtWidgets.QSplashScreen(splash_pix)
            # splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
            # splash.setEnabled(False)
            # # adding progress bar
            # progressBar = QtWidgets.QProgressBar(splash)
            # progressBar.setMaximum(10)
            # progressBar.setGeometry(130, splash_pix.height() - 100, splash_pix.width() - 250, 20)
            # progressBar.setStyleSheet("QProgressBar::chunk"
            #                           "{"
            #                           "background-color: red;"
            #                           "}")

            # splash.setMask(splash_pix.mask())

            # splash.show()

            # for i in range(1, 11):
            #     progressBar.setValue(i)
            #     t = time.time()
            #     while time.time() < t + 0.1:
            #         app.processEvents()

            # # Simulate something that takes time
            # time.sleep(1)

            # splash.finish(vt_launcher_ui)

            vt_launcher_ui.show()
            vt_launcher_ui.resize(500, 500)
            vt_launcher_ui.setup_ui()
            # vt_launcher_ui.update_cls = update.Update(parent_window=vt_launcher_ui)
            sys.exit(app.exec())
        else:
            error_message = QtWidgets.QMessageBox()
            error_message.setIcon(QtWidgets.QMessageBox.Warning)
            error_message.setWindowTitle("Error")
            error_message.setText("The application is already running!")
            error_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_message.exec()
    finally:
        lock_file.unlock()
