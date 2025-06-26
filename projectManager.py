import winreg
from ui.projectManagerWidget import ProjectManagerWidget
from commands import Commands


class ProjectManager(ProjectManagerWidget):
    def __init__(self, parent=None):
        super(ProjectManager, self).__init__(parent=parent)
        self.parent = parent
        self.project_info: dict = {}
        self.db = None

        self.connect_signals()

    def get_installed_engines(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\EpicGames\Unreal Engine")
            i = 0
            while True:
                try:
                    subkey = winreg.EnumKey(key, i)
                    yield "UE_" + subkey
                    i += 1
                except WindowsError as e:
                    break
        except Exception as e:
            print(e)

    def set_ui(self, ):
        engines = self.get_installed_engines()
        engine_list = list(engines)
        if not engine_list:
            engine_list = ["UE_5.4", "UE_5.5", "UE_5.6",]
        self.comboBox_engine_version.clear()
        self.comboBox_engine_version.addItems(engine_list)
        self.le_project_name.setText(self.project_info["name"])
        self.le_project_name_korean.setText(self.project_info["name_korean"])
        self.comboBox_engine_version.setCurrentText(self.project_info.get("engine_version", ""))
        self.le_content_path.setText(self.project_info.get("content_path", ""))
        self.le_resource_path.setText(self.project_info.get("resource_path", ""))
        self.checkbox_finished.setChecked(self.project_info.get("finished", False))

    def connect_signals(self):
        self.combobox_projects.currentIndexChanged.connect(self.update_project_info)
        self.new_project_button.clicked.connect(self.create_new_project)
        # self.del_project_button.clicked.connect(self.delete_project)
        self.save_button.clicked.connect(self.update_project_data)
        self.del_project_button.clicked.connect(lambda x: self.update_project_data("delete"))

    def disconnect_signals(self):
        try:
            self.combobox_projects.currentIndexChanged.disconnect()
        except RuntimeError as e:
            pass
        self.new_project_button.clicked.disconnect()

    def update_project_info(self):
        # current_project = self.combobox_projects.currentText().split(" ")[0]
        current_project = self.combobox_projects.currentText().rsplit(" (", 1)[0]
        project_info = self.db.get_project_data(current_project)
        self.project_info = project_info
        if project_info:
            self.set_ui()

    def create_new_project(self):
        self.project_info = {}
        self.le_project_name.clear()
        self.le_project_name_korean.clear()
        self.le_content_path.setText("//depot/{project}/{sub_project}")
        self.le_resource_path.setText("//Resource/{project}/{sub_project}")

        self.new_project_button.setText("취소")
        self.disconnect_signals()
        self.del_project_button.setEnabled(False)
        self.new_project_button.clicked.connect(self.set_default)

    def set_default(self):
        self.update_project_info()
        self.new_project_button.setText("새 프로젝트")
        self.new_project_button.clicked.disconnect()
        self.del_project_button.setEnabled(True)
        self.combobox_projects.currentIndexChanged.connect(self.update_project_info)
        self.new_project_button.clicked.connect(self.create_new_project)

    def update_project_data(self, delete=""):
        # self.project_info.update({"delete": delete})
        self.project_info.update({"name": self.le_project_name.text()})
        self.project_info.update({"name_korean": self.le_project_name_korean.text()})
        self.project_info.update({"engine_version": self.comboBox_engine_version.currentText()})
        self.project_info.update({"content_path": self.le_content_path.text()})
        self.project_info.update({"resource_path": self.le_resource_path.text()})
        self.project_info.update({"finished": self.checkbox_finished.isChecked()})

        if delete == "delete":
            result = self.question_widget("프로젝트를 삭제 하시겠습니까?")
            if not result:
                return
            resp = Commands().delete_project(self.project_info)
        else:
            resp = Commands().save_project(self.project_info)
        
        if resp:
            self.del_project_button.setEnabled(True)
            self.del_project_button.setText("프로젝트 삭제")
            self.message_widget()
            self.set_default()
            self.parent.update_projects()
        else:
            self.message_widget(False)


