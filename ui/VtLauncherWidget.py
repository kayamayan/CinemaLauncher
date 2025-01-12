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
	border-radius: 5px;	
	background-color: rgb(56, 56, 56);
}
QPushButton:hover {
	background-color: rgb(94, 94, 94);
	border: 2px solid rgb(94, 94, 94);
}
QPushButton:pressed {	
	background-color: rgb(45, 45, 45);
	border: 2px solid rgb(45, 45, 45);
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
"""

stylesheet = stylesheet.replace("RESOURCE_DIR", RESOURCE_DIR)


class VtLauncherWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(VtLauncherWidget, self).__init__(parent=parent)
        self.setStyleSheet(stylesheet)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QtWidgets.QFrame(self)
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_project = QtWidgets.QFrame(self.frame_main)
        self.frame_project.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.frame_project.setFont(font)
        # self.frame_project.setStyleSheet("background: transparent;")
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
        self.verticalLayout_4.addWidget(self.frame_project)

        finished_checkbox_layout = QtWidgets.QHBoxLayout(self.frame_main)
        self.show_finished_checkbox = QtWidgets.QCheckBox("마감된 프로젝트 보기")
        spacer_item = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        finished_checkbox_layout.addItem(spacer_item)
        finished_checkbox_layout.addWidget(self.show_finished_checkbox)
        self.verticalLayout_4.addLayout(finished_checkbox_layout)

        self.frame_buttons = QtWidgets.QFrame(self.frame_main)
        # self.frame_buttons.setStyleSheet("background: transparent;")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_buttons)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_sync_launch = QtWidgets.QPushButton(self.frame_buttons)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_sync_launch.sizePolicy().hasHeightForWidth())
        self.btn_sync_launch.setSizePolicy(size_policy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(CURRENT_DIR + "/resource/icons/p4v_ue.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btn_sync_launch.setIcon(icon)
        self.btn_sync_launch.setIconSize(QtCore.QSize(120, 60))
        # self.btn_sync_launch.setStyleSheet("background-position: center;\n"
        #                                    "background-repeat: no-repeat;")
        self.btn_sync_launch.setText("")
        self.verticalLayout_5.addWidget(self.btn_sync_launch)
        self.btn_launch = QtWidgets.QPushButton(self.frame_buttons)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_launch.sizePolicy().hasHeightForWidth())
        self.btn_launch.setSizePolicy(size_policy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(CURRENT_DIR + "/resource/icons/ue_60.png"))
        self.btn_launch.setIcon(icon)
        self.btn_launch.setIconSize(QtCore.QSize(60, 60))
        self.btn_launch.setStyleSheet("background-position: center;\n"
                                      "background-repeat: no-repeat;")
        self.btn_launch.setText("")
        self.btn_launch.setObjectName("btn_launch")
        self.verticalLayout_5.addWidget(self.btn_launch)
        self.btn_sync = QtWidgets.QPushButton(self.frame_buttons)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_sync.sizePolicy().hasHeightForWidth())
        self.btn_sync.setSizePolicy(size_policy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(CURRENT_DIR + "/resource/icons/p4v_60.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btn_sync.setIcon(icon)
        self.btn_sync.setIconSize(QtCore.QSize(60, 60))
        self.btn_sync.setStyleSheet("background-position: center;\n"
                                    "background-repeat: no-repeat;")
        self.btn_sync.setText("")
        self.btn_sync.setObjectName("btn_sync")
        self.verticalLayout_5.addWidget(self.btn_sync)
        self.btn_open_content = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_open_content.setText("open content dir")
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_open_content.sizePolicy().hasHeightForWidth())
        self.btn_open_content.setSizePolicy(size_policy)
        self.btn_open_content.setObjectName("btn_open_content")
        self.verticalLayout_5.addWidget(self.btn_open_content)
        self.btn_open_resource = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_open_resource.setText("open resource dir")
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_open_resource.sizePolicy().hasHeightForWidth())
        self.btn_open_resource.setSizePolicy(size_policy)
        self.btn_open_resource.setObjectName("btn_open_resource")
        self.verticalLayout_5.addWidget(self.btn_open_resource)

        self.verticalLayout_4.addWidget(self.frame_buttons)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)
