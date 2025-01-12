# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/kayamayan.NC-KOREA/Documents/visual_tech/apps/VtLauncher/ui/VtLauncherWidget.ui',
# licensing of 'C:/Users/kayamayan.NC-KOREA/Documents/visual_tech/apps/VtLauncher/ui/VtLauncherWidget.ui' applies.
#
# Created: Mon Apr 18 11:02:29 2022
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

import os
from PySide2 import QtCore, QtGui, QtWidgets

CURRENT_DIR = os.path.dirname(__file__).replace("\\", '/')
RESOURCE_DIR = CURRENT_DIR + "/resource"

stylesheet = """
QPushButton {
	border: 2px solid rgb(56, 56, 56);
	border-radius: 2px;	
	background-color: rgb(56, 56, 56);
	height: 15px;
	width: 80;
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


class ProjectManagerWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ProjectManagerWidget, self).__init__(parent=parent)
        self.setStyleSheet(stylesheet)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QtWidgets.QFrame(self)
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        main_layout = QtWidgets.QVBoxLayout(self.frame_main)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_project = QtWidgets.QFrame(self.frame_main)
        self.frame_project.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_project.setFont(font)
        self.frame_project.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_project.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_project.setObjectName("frame_project")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_project)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_project = QtWidgets.QLabel(self.frame_project)
        self.label_project.setText("프로젝트")
        self.label_project.setMaximumSize(QtCore.QSize(50, 200))
        self.label_project.setObjectName("label_project")
        self.horizontalLayout.addWidget(self.label_project)
        self.combobox_projects = QtWidgets.QComboBox(self.frame_project)
        self.combobox_projects.setObjectName("combobox_projects")
        self.combobox_projects.setMinimumSize(QtCore.QSize(0, 30))
        self.combobox_projects.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.horizontalLayout.addWidget(self.combobox_projects)
        self.btn_refersh_project = QtWidgets.QPushButton(self.frame_project)
        self.btn_refersh_project.setText("새로고침")
        self.btn_refersh_project.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btn_refersh_project.setMinimumHeight(30)
        self.btn_refersh_project.setObjectName("btn_refersh_project")
        self.horizontalLayout.addWidget(self.btn_refersh_project)
        main_layout.addWidget(self.frame_project)

        finished_checkbox_layout = QtWidgets.QHBoxLayout(self.frame_main)
        self.show_finished_checkbox = QtWidgets.QCheckBox("마감된 프로젝트 보기")
        spacer_item = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        finished_checkbox_layout.addItem(spacer_item)
        finished_checkbox_layout.addWidget(self.show_finished_checkbox)
        main_layout.addLayout(finished_checkbox_layout)

        main_layout.addWidget(self.h_line())
        self.frame_top_button = QtWidgets.QFrame(self.frame_main)
        frame_top_layout = QtWidgets.QHBoxLayout(self.frame_top_button)
        frame_top_layout.setContentsMargins(0, 10, 0, 0)
        button_font = QtGui.QFont()
        button_font.setFamily("Segoe UI")
        button_font.setBold(True)
        self.new_project_button = QtWidgets.QPushButton("새 프로젝트")
        self.new_project_button.setFont(button_font)
        self.new_project_button.setMinimumSize(100, 30)
        self.new_project_button.setStyleSheet("QPushButton {"
                                              # "border: 2px solid rgb(56, 56, 56);\n"
                                              "border-radius: 3px;"
                                              "background-color: rgb(117, 121, 235);"
                                              "}"
                                              "QPushButton:hover {"
                                              "background-color: rgb(91, 94, 183);"
                                              # "border: 2px solid rgb(94, 94, 94);\n"
                                              "}"
                                              "QPushButton:pressed {"
                                              "background-color: rgb(65, 67, 131);"
                                              # "border: 2px solid rgb(43, 50, 61);\n"
                                              "}")
        frame_top_layout.addWidget(self.new_project_button)
        self.del_project_button = QtWidgets.QPushButton("프로젝트 삭제")
        self.del_project_button.setFont(button_font)
        self.del_project_button.setMinimumSize(100, 30)
        self.del_project_button.setStyleSheet("QPushButton {"
                                              # "border: 2px solid rgb(56, 56, 56);\n"
                                              "border-radius: 3px;"
                                              "background-color: rgb(255, 107, 102);"
                                              "}"
                                              "QPushButton:hover {"
                                              "background-color: rgb(204, 85, 81);"
                                              # "border: 2px solid rgb(94, 94, 94);\n"
                                              "}"
                                              "QPushButton:pressed {"
                                              "background-color: rgb(127, 53, 50);"
                                              # "border: 2px solid rgb(43, 50, 61);\n"
                                              "}")
        frame_top_layout.addWidget(self.del_project_button)
        spacer_item = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        frame_top_layout.addItem(spacer_item)
        self.save_button = QtWidgets.QPushButton("저장")
        self.save_button.setFont(button_font)
        self.save_button.setMinimumSize(100, 30)
        self.save_button.setStyleSheet("QPushButton {"
                                       # "border: 2px solid rgb(56, 56, 56);\n"
                                       "border-radius: 3px;"
                                       "background-color: rgb(117, 121, 235);"
                                       "}"
                                       "QPushButton:hover {"
                                       "background-color: rgb(91, 94, 183);"
                                       # "border: 2px solid rgb(94, 94, 94);\n"
                                       "}"
                                       "QPushButton:pressed {"
                                       "background-color: rgb(65, 67, 131);"
                                       # "border: 2px solid rgb(43, 50, 61);\n"
                                       "}")
        frame_top_layout.addWidget(self.save_button)
        main_layout.addWidget(self.frame_top_button)

        self.frame_content = QtWidgets.QFrame(self.frame_main)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.content_layout = QtWidgets.QVBoxLayout(self.frame_content)
        self.content_layout.setObjectName("content_layout")
        self.frame_name = QtWidgets.QFrame(self.frame_content)
        self.frame_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_name.setObjectName("frame_name")
        self.frame_name_layout = QtWidgets.QHBoxLayout(self.frame_name)
        self.frame_name_layout.setObjectName("frame_name_layout")
        self.frame_name_layout.setContentsMargins(0, 0, 0, 0)
        self.label_project_name = QtWidgets.QLabel(self.frame_name)
        self.label_project_name.setText("프로젝트 이름")
        self.label_project_name.setMinimumSize(QtCore.QSize(80, 0))
        self.label_project_name.setObjectName("label_project_name")
        self.label_project_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.frame_name_layout.addWidget(self.label_project_name)
        self.le_project_name = QtWidgets.QLineEdit(self.frame_name)
        self.le_project_name.setMinimumSize(QtCore.QSize(0, 0))
        self.le_project_name.setObjectName("le_project_name")
        self.frame_name_layout.addWidget(self.le_project_name)
        # spacer_item = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.frame_name_layout.addItem(spacer_item)
        self.content_layout.addWidget(self.frame_name)

        self.frame_name_korean = QtWidgets.QFrame(self.frame_content)
        self.frame_name_korean.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_name_korean.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_name_korean.setObjectName("frame_name_korean")
        self.frame_name_korean_layout = QtWidgets.QHBoxLayout(self.frame_name_korean)
        self.frame_name_korean_layout.setObjectName("frame_name_korean_layout")
        self.frame_name_korean_layout.setContentsMargins(0, 0, 0, 0)
        self.label_project_name_korean = QtWidgets.QLabel(self.frame_name_korean)
        self.label_project_name_korean.setText("한글 이름")
        self.label_project_name_korean.setMinimumSize(QtCore.QSize(80, 0))
        self.label_project_name_korean.setObjectName("label_project_name_korean")
        self.label_project_name_korean.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.frame_name_korean_layout.addWidget(self.label_project_name_korean)
        self.le_project_name_korean = QtWidgets.QLineEdit(self.frame_name)
        self.le_project_name_korean.setMinimumSize(QtCore.QSize(0, 0))
        self.le_project_name_korean.setObjectName("le_project_name_korean")
        self.frame_name_korean_layout.addWidget(self.le_project_name_korean)
        # spacer_item = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.frame_name_korean_layout.addItem(spacer_item)
        self.content_layout.addWidget(self.frame_name_korean)

        self.frame_engine_version = QtWidgets.QFrame(self.frame_content)
        self.frame_engine_version.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_engine_version.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_engine_version.setObjectName("frame_engine_version")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_engine_version)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_engine_version = QtWidgets.QLabel(self.frame_engine_version)
        self.label_engine_version.setText("엔진 버전")
        self.label_engine_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_engine_version.setMinimumSize(QtCore.QSize(80, 0))
        self.label_engine_version.setObjectName("label_engine_version")
        self.horizontalLayout_3.addWidget(self.label_engine_version)
        self.comboBox_engine_version = QtWidgets.QComboBox(self.frame_engine_version)
        self.comboBox_engine_version.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_engine_version.setObjectName("comboBox_engine_version")
        self.horizontalLayout_3.addWidget(self.comboBox_engine_version)
        spacer_item1 = QtWidgets.QSpacerItem(187, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacer_item1)
        self.content_layout.addWidget(self.frame_engine_version)

        self.frame_content_path = QtWidgets.QFrame(self.frame_content)
        self.frame_content_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_path.setObjectName("frame_content_path")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_content_path)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_content_path = QtWidgets.QLabel(self.frame_content_path)
        self.label_content_path.setText("컨텐츠 경로")
        self.label_content_path.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_content_path.setMinimumSize(QtCore.QSize(80, 0))
        self.label_content_path.setObjectName("label_content_path")
        self.horizontalLayout_4.addWidget(self.label_content_path)
        self.le_content_path = QtWidgets.QLineEdit(self.frame_content_path)
        self.le_content_path.setObjectName("le_content_path")
        self.horizontalLayout_4.addWidget(self.le_content_path)
        # self.btn_content_path = QtWidgets.QPushButton(self.frame_content_path)
        # self.btn_content_path.setText("Browse")
        # self.btn_content_path.setObjectName("btn_content_path")
        # self.horizontalLayout_4.addWidget(self.btn_content_path)
        self.content_layout.addWidget(self.frame_content_path)

        self.frame_resource_path = QtWidgets.QFrame(self.frame_content)
        self.frame_resource_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_resource_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_resource_path.setObjectName("frame_resource_path")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_resource_path)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_resource_path = QtWidgets.QLabel(self.frame_resource_path)
        self.label_resource_path.setText("리소스 경로")
        self.label_resource_path.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_resource_path.setMinimumSize(QtCore.QSize(80, 0))
        self.label_resource_path.setObjectName("label_resource_path")
        self.horizontalLayout_5.addWidget(self.label_resource_path)
        self.le_resource_path = QtWidgets.QLineEdit(self.frame_resource_path)
        self.le_resource_path.setObjectName("le_resource_path")
        self.horizontalLayout_5.addWidget(self.le_resource_path)
        self.content_layout.addWidget(self.frame_resource_path)

        self.frame_finished = QtWidgets.QFrame(self.frame_content)
        self.frame_finished.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_finished.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_finished.setObjectName("frame_finished")
        layout_finished = QtWidgets.QHBoxLayout(self.frame_finished)
        layout_finished.setContentsMargins(0, 0, 0, 0)
        label_finished = QtWidgets.QLabel(self.frame_finished)
        label_finished.setText("완료")
        label_finished.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        label_finished.setMinimumSize(QtCore.QSize(80, 0))
        layout_finished.addWidget(label_finished)
        self.checkbox_finished = QtWidgets.QCheckBox(self.frame_finished)
        self.checkbox_finished.setObjectName("le_finished")
        layout_finished.addWidget(self.checkbox_finished)
        layout_finished.addStretch()
        self.content_layout.addWidget(self.frame_finished)

        spacer_item2 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.content_layout.addItem(spacer_item2)

        main_layout.addWidget(self.frame_content)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)

    def h_line(self):
        """seporator line for widgets

        Returns:
            Qframe: line for seperating UI elements visually
        """
        seperator_line = QtWidgets.QFrame()
        seperator_line.setFrameShape(QtWidgets.QFrame.HLine)
        seperator_line.setFrameShadow(QtWidgets.QFrame.Plain)
        seperator_line.setStyleSheet("color: rgb(30, 30, 30);")
        return seperator_line

    def message_widget(self, success=True):
        if success:
            QtWidgets.QMessageBox.information(self, "성공", "완료.")
        else:
            QtWidgets.QMessageBox.critical(self, "실패", "실패.")

    def question_widget(self, message):
        result = QtWidgets.QMessageBox.question(self, "확인", message,
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False
