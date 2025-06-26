# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
from PySide6 import QtCore, QtGui, QtWidgets

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


class UpdateWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UpdateWidget, self).__init__(parent)
        self.resize(312, 97)
        self.setStyleSheet(stylesheet)
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
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item)
        self.main_layout.addLayout(self.horizontalLayout_2)
        self.download_progressBar = QtWidgets.QProgressBar(self)
        self.download_progressBar.setValue(0)
        self.download_progressBar.setObjectName("download_progressBar")
        self.main_layout.addWidget(self.download_progressBar)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setObjectName("horizontalLayout")
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
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
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        button_layout.addItem(spacer_item2)
        self.main_layout.addLayout(button_layout)

        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("Form", "Software Update", None, -1))
        self.label.setText(
            QtWidgets.QApplication.translate("Form", "\n  업데이트가 있습니다.\n"
                                                     "\n  기존파일을 덮어쓰고 자동으로 실행됩니다.\n", None, -1)
        )
        self.update_pushButton.setText(QtWidgets.QApplication.translate("Form", "Download File", None, -1))
        self.cancel_pushButton.setText(QtWidgets.QApplication.translate("Form", "Cancel", None, -1))
