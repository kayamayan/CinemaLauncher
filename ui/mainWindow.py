# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/kayamayan.NC-KOREA/Documents/visual_tech/apps/VtLauncher/ui/mainWindow.ui',
# licensing of 'C:/Users/kayamayan.NC-KOREA/Documents/visual_tech/apps/VtLauncher/ui/mainWindow.ui' applies.
#
# Created: Mon Apr 18 11:02:20 2022
#      by: PySide6-uic  running on PySide6 5.12.5
#
# WARNING! All changes made in this file will be lost!

import os
from PySide6 import QtCore, QtGui, QtWidgets

from .VtLauncherWidget import VtLauncherWidget
from projectManager import ProjectManager
from .settingsWidget import SettingWidget
from uiStyle import Style

CURRENT_DIR = os.path.dirname(__file__).replace("\\", '/')
RESOURCE_DIR = CURRENT_DIR + "/resource"


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)
        icon_pixmap = QtGui.QPixmap(CURRENT_DIR + "/resource/icons/vt_logo_inverse.png")
        icon = QtGui.QIcon()
        icon.addPixmap(icon_pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setWindowIcon(icon)
        self.setObjectName("MainWindow")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.setFont(font)
        self.setStyleSheet(Style.style_main)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setStyleSheet("background: transparent;\n"
                                          "color: rgb(210, 210, 210);")
        self.central_widget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_main = QtWidgets.QFrame(self.central_widget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.top_button_frame = QtWidgets.QFrame(self.frame_top)
        self.top_button_frame.setMaximumSize(QtCore.QSize(16777215, 42))
        self.top_button_frame.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.top_button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_button_frame.setObjectName("top_button_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.top_button_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.top_button_frame)
        self.frame.setStyleSheet("background: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_btns_right = QtWidgets.QFrame(self.top_button_frame)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_btns_right.setStyleSheet("background: transparent;")
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(size_policy)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_minimize.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
                                        "    border: none;\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(56, 56, 56);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}")
        self.btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(CURRENT_DIR + "/resource/icons/20x20/cil-window-minimize.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_4.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(size_policy)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_close.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {    \n"
                                     "    border: none;\n"
                                     "    background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(56, 56, 56);\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "}")
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(CURRENT_DIR + "/resource/icons/20x20/cil-x.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_4.addWidget(self.btn_close)
        self.horizontalLayout_5.addWidget(self.frame_btns_right)
        self.horizontalLayout_3.addWidget(self.top_button_frame)
        # self.verticalLayout_3.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.frame_center)
        self.frame_left_menu.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.frame_left_menu.setMinimumSize(QtCore.QSize(110, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(110, 16777215))
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.left_menu_layout = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.left_menu_layout.setSpacing(0)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setObjectName("verticalLayout_5")

        self.tab_vtlauncher_button = QtWidgets.QPushButton(self.frame_left_menu)
        self.tab_vtlauncher_button.setText("Cinema Launcher")
        self.tab_vtlauncher_button.setFont(font)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.tab_vtlauncher_button.sizePolicy().hasHeightForWidth())
        self.tab_vtlauncher_button.setSizePolicy(size_policy)
        self.tab_vtlauncher_button.setMinimumSize(QtCore.QSize(0, 50))
        self.tab_vtlauncher_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tab_vtlauncher_button.setStyleSheet("QPushButton {\n"
                                                 "    background-position: center;\n"
                                                 "    background-repeat: no-reperat;\n"
                                                 "    border: none;\n"
                                                 "    background-color: rgb(25, 25, 25);\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(33, 37, 43);\n"
                                                 "}\n"
                                                 "QPushButton:pressed {    \n"
                                                 "    background-color: rgb(85, 170, 255);\n"
                                                 "}")
        self.tab_vtlauncher_button.setObjectName("tab_vtlauncher_button")

        self.tab_project_manager_button = QtWidgets.QPushButton(self.frame_left_menu)
        self.tab_project_manager_button.setText("Project Manager")
        self.tab_project_manager_button.setFont(font)
        self.tab_project_manager_button.setSizePolicy(size_policy)
        self.tab_project_manager_button.setMinimumSize(QtCore.QSize(0, 50))
        self.tab_project_manager_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tab_project_manager_button.setStyleSheet("QPushButton {\n"
                                                      "    background-position: center;\n"
                                                      "    background-repeat: no-reperat;\n"
                                                      "    border: none;\n"
                                                      "    background-color: rgb(25, 25, 25);\n"
                                                      "}\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: rgb(33, 37, 43);\n"
                                                      "}\n"
                                                      "QPushButton:pressed {    \n"
                                                      "    background-color: rgb(85, 170, 255);\n"
                                                      "}")
        self.tab_project_manager_button.setObjectName("tab_project_manager_button")

        self.left_menu_layout.addWidget(self.tab_vtlauncher_button)
        self.left_menu_layout.addWidget(self.tab_project_manager_button)
        spacer_item = QtWidgets.QSpacerItem(20, 429, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.left_menu_layout.addItem(spacer_item)

        extra_button_frame = QtWidgets.QFrame(self.frame_left_menu)
        extra_button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        extra_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        extra_button_layout = QtWidgets.QHBoxLayout(extra_button_frame)
        extra_button_layout.setSpacing(10)
        extra_button_layout.setContentsMargins(0, 0, 0, 0)

        self.label_user = QtWidgets.QLabel(extra_button_frame)
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setText("User")
        self.label_user.setMinimumSize(QtCore.QSize(60, 60))
        self.label_user.setMaximumSize(QtCore.QSize(60, 60))
        self.label_user.setStyleSheet("QLabel {\n"
                                      "   border-radius: 30px;\n"
                                      "   background-color: rgb(44, 49, 60);\n"
                                      "   border: 5px solid rgb(39, 44, 54);\n"
                                      "   background-position: center;\n"
                                      "   background-repeat: no-repeat;\n"
                                      "}")

        self.settings_button = QtWidgets.QPushButton(self.frame_left_menu)
        self.settings_button.setObjectName("settings_button")
        # self.settings_button.setText("Settings")
        self.settings_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.settings_button.setIcon(
            QtGui.QIcon(QtGui.QPixmap(CURRENT_DIR + "/resource/icons/24x24/cil-settings.png"))
        )
        self.settings_button.setIconSize(QtCore.QSize(24, 24))
        self.settings_button.setFlat(False)
        self.settings_button.setMinimumSize(QtCore.QSize(0, 50))
        self.settings_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.settings_button.setStyleSheet("QPushButton {\n"
                                           "    background-position: center;\n"
                                           "    background-repeat: no-reperat;\n"
                                           "    border: none;\n"
                                           "    background-color: rgb(25, 25, 25);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(33, 37, 43);\n"
                                           "}\n"
                                           "QPushButton:pressed {    \n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")

        extra_button_layout.addWidget(self.label_user)

        self.left_menu_layout.addWidget(extra_button_frame)
        self.left_menu_layout.addWidget(self.settings_button)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_content_right = QtWidgets.QFrame(self.frame_center)
        self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.layout_content_right = QtWidgets.QVBoxLayout(self.frame_content_right)
        self.layout_content_right.setSpacing(0)
        self.layout_content_right.setContentsMargins(0, 0, 0, 0)
        self.layout_content_right.setObjectName("layout_content_right")
        self.stacked_widget = QtWidgets.QStackedWidget(self.frame_content_right)
        self.under_bar = QtWidgets.QFrame(self.frame_content_right)
        self.under_bar.setMinimumHeight(30)

        self.vtLauncher_widget = VtLauncherWidget()
        self.project_manager = ProjectManager(self)
        self.settings_widget = SettingWidget(self)
        self.settings_widget.setStyleSheet(Style.style_main)

        self.stacked_widget.addWidget(self.vtLauncher_widget)
        self.stacked_widget.addWidget(self.project_manager)
        self.stacked_widget.addWidget(self.settings_widget)

        self.layout_content_right.addWidget(self.stacked_widget)
        self.layout_content_right.addWidget(self.under_bar)
        self.horizontalLayout_2.addWidget(self.frame_content_right)
        self.verticalLayout_3.addWidget(self.frame_center)
        self.horizontalLayout.addWidget(self.frame_main)
        self.setCentralWidget(self.central_widget)

        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
