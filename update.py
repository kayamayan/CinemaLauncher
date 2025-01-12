import os
import sys
import win32api
from PySide2 import QtCore, QtWidgets, QtGui

CURRENT_DIR = os.path.dirname(__file__).replace("\\", '/')
RESOURCE_DIR = CURRENT_DIR + "/resource"

stylesheet = """
QWidget {
    background-color: rgb(25, 25, 25);
    color: rgb(210, 210, 210);
}
QPushButton {
	border: 2px solid rgb(56, 56, 56);
	border-radius: 5px;	
	background-color: rgb(56, 56, 56);
}
QPushButton:hover {
	background-color: rgb(56, 56, 56);
	border: 2px solid rgb(94, 94, 94);
}
QPushButton:pressed {	
	background-color: rgb(35, 40, 49);
	border: 2px solid rgb(43, 50, 61);
}
QComboBox{
	background-color: rgb(25, 25, 25);
	border-radius: 5px;
	border: 2px solid rgb(25, 25, 25);
	padding: 5px;
	padding-left: 10px;
}
QComboBox:hover{
	border: 2px solid rgb(64, 71, 88);
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px;
    border-left-width: 3px;
    border-left-color: rgba(39, 44, 54, 150);
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    background-image: url(RESOURCE_DIR/icons/16x16/cil-arrow-bottom.png);
    background-position: center;
    background-repeat: no-reperat;
 }
QComboBox QAbstractItemView {
	color: rgb(85, 170, 255);	
	background-color: rgb(25, 25, 25);
	padding: 10px;
	selection-background-color: rgb(39, 44, 54);
}
QComboBox QAbstractItemView::item {
    min-height: 20px;
    min-width: 50px;
}
QLineEdit {
	background-color: rgb(25, 25, 25);
	border-radius: 5px;
	border: 2px solid rgb(25, 25, 25);
	padding-left: 10px;
}
QLineEdit:hover {
	border: 2px solid rgb(64, 71, 88);
}
QLineEdit:focus {
	border: 2px solid rgb(91, 101, 124);
}
"""

stylesheet = stylesheet.replace("RESOURCE_DIR", RESOURCE_DIR)
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
CURRENT_EXE = os.path.join(CURRENT_PATH, "VtLauncher.exe")
SERVER_EXE = r"\\cinemaserver\Tcinema\VTLIB\apps\VtLauncher\dist\VtLauncher.exe"


class ProgressThread(QtCore.QThread):
    progress_update = QtCore.Signal(int)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        self.copy(SERVER_EXE, CURRENT_EXE)
        # subprocess.Popen(fr'explorer /select,"{tmp_file}"')
        # self.progress_done.emit(True)

    def copy(self, src, dst):
        source_size = os.stat(src).st_size
        copied = 0

        with open(src, "rb") as source, open(dst, "wb") as target:
            while True:
                chunk = source.read(1024)
                if not chunk:
                    break
                target.write(chunk)
                copied += len(chunk)
                self.progress_update.emit(copied * 100 / source_size)


class Update(QtWidgets.QWidget):
    def __init__(self, parent=None, version=None):
        super(Update, self).__init__(parent)
        self._version = version
        self.progress_thread = ProgressThread()

        self.resize(312, 97)
        # self.setStyleSheet(stylesheet)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QtWidgets.QFrame(self)
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.main_layout = QtWidgets.QVBoxLayout(self.frame_main)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 10, 0)
        self.main_layout.setObjectName("main_layout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item)
        self.main_layout.addLayout(self.horizontalLayout_2)
        self.download_progressBar = QtWidgets.QProgressBar(self)
        self.download_progressBar.setValue(0)
        self.download_progressBar.setObjectName("download_progressBar")
        self.main_layout.addWidget(self.download_progressBar)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setObjectName("horizontalLayout")
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        button_layout.addItem(spacer_item1)
        self.update_pushButton = QtWidgets.QPushButton(self)
        self.update_pushButton.setObjectName("update_pushButton")
        self.update_pushButton.setFixedSize(100, 30)
        button_layout.addWidget(self.update_pushButton)
        button_layout.addItem(spacer_item)
        self.cancel_pushButton = QtWidgets.QPushButton(self)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.cancel_pushButton.setFixedSize(100, 30)
        button_layout.addWidget(self.cancel_pushButton)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        button_layout.addItem(spacer_item2)
        self.main_layout.addLayout(button_layout)

        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        self.update_pushButton.clicked.connect(self.progress_thread.start)
        self.cancel_pushButton.clicked.connect(self.close_ui)

        self.progress_thread.progress_update.connect(self.update_progress_bar)
        self.progress_thread.finished.connect(self.finished)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("Form", "Software Update", None, -1))
        self.label.setText(
            QtWidgets.QApplication.translate("Form", "\n  업데이트.\n", None, -1)
        )
        self.update_pushButton.setText(QtWidgets.QApplication.translate("Form", "Download File", None, -1))
        self.cancel_pushButton.setText(QtWidgets.QApplication.translate("Form", "Cancel", None, -1))

    @QtCore.Slot(float)
    def update_progress_bar(self, maxVal):
        self.download_progressBar.setValue(maxVal)

    def finished(self):
        win32api.ShellExecute(0, 'open', CURRENT_EXE, None, "", 1)
        self.close_ui()
        # os.system("start " + CURRENT_EXE)
        # self.parent_window.close_ui()

    def close_ui(self):
        self.close()


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-v', '--version', help='version', required=True)
    # args = parser.parse_args()
    app = QtWidgets.QApplication(sys.argv)
    window = Update()
    window.show()
    sys.exit(app.exec_())
