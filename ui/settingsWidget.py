# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/kayamayan.NC-KOREA/Documents/visual_tech/apps/VtLauncher/ui/settingsWidget.ui',
# licensing of 'C:/Users/kayamayan.NC-KOREA/Documents/visual_tech/apps/VtLauncher/ui/settingsWidget.ui' applies.
#
# Created: Tue Apr 26 14:55:16 2022
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

import os
import subprocess
from PySide2 import QtCore, QtGui, QtWidgets

import config

CURRENT_DIR = os.path.dirname(__file__).replace("\\", '/')
RESOURCE_DIR = CURRENT_DIR + "/resource"

stylesheet = """
QTabWidget::pane {
    border-top: 3px solid #535a57;
}

QTabWidget:movable {
    background: #ff7500;
}

QTabBar::tab {
    background: #535a57;
    min-width: 8ex;
    padding: 5px 10px;
}

QTabBar::tab:hover {
    background: #6fc2ff;
}

QTabBar::tab:movable {
    background: #ff7500;
}

QTabBar::tab:selected {
    background: #0094ff;
}

QTabBar::tab:!selected {
    margin-top: 5px;
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


class SettingWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SettingWidget, self).__init__(parent=parent)
        self.parent = parent

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QtWidgets.QFrame(self)
        self.frame_main.setStyleSheet(stylesheet)
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings_tab_widget = QtWidgets.QTabWidget(self.frame_main)
        self.settings_tab_widget.setObjectName("settings_tab_widget")
        self.tab_general_option = QtWidgets.QWidget()
        self.tab_general_option.setObjectName("tab_general_option")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_general_option)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_general_2 = QtWidgets.QFrame(self.tab_general_option)
        self.frame_general_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_general_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_general_2.setObjectName("frame_general_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_general_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_11 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_engine_root = QtWidgets.QLabel(self.frame_11)
        self.label_engine_root.setMinimumSize(QtCore.QSize(150, 30))
        self.label_engine_root.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_engine_root.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_engine_root.setObjectName("label_engine_root")
        self.horizontalLayout_16.addWidget(self.label_engine_root)
        self.engine_path_line_edit = QtWidgets.QLineEdit(self.frame_11)
        self.engine_path_line_edit.setObjectName("engine_path_line_edit")
        self.horizontalLayout_16.addWidget(self.engine_path_line_edit)
        self.btn_browse_engine_dir = QtWidgets.QPushButton(self.frame_11)
        self.btn_browse_engine_dir.setMinimumSize(QtCore.QSize(23, 0))
        self.btn_browse_engine_dir.setMaximumSize(QtCore.QSize(23, 16777215))
        self.btn_browse_engine_dir.setObjectName("btn_browse_engine_dir")
        self.horizontalLayout_16.addWidget(self.btn_browse_engine_dir)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_16 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_enable_dx12 = QtWidgets.QLabel(self.frame_16)
        self.label_enable_dx12.setMinimumSize(QtCore.QSize(150, 30))
        self.label_enable_dx12.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_enable_dx12.setText("")
        self.label_enable_dx12.setObjectName("label_enable_dx12")
        self.horizontalLayout_17.addWidget(self.label_enable_dx12)
        self.checkbox_enable_dx12 = QtWidgets.QCheckBox(self.frame_16)
        self.checkbox_enable_dx12.setObjectName("checkbox_enable_dx12")
        self.horizontalLayout_17.addWidget(self.checkbox_enable_dx12)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_p4_exe = QtWidgets.QLabel(self.frame_17)
        self.label_p4_exe.setMinimumSize(QtCore.QSize(150, 30))
        self.label_p4_exe.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_p4_exe.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_p4_exe.setObjectName("label_p4_exe")
        self.horizontalLayout_18.addWidget(self.label_p4_exe)
        self.p4_path_line_edit = QtWidgets.QLineEdit(self.frame_17)
        self.p4_path_line_edit.setObjectName("p4_path_line_edit")
        self.horizontalLayout_18.addWidget(self.p4_path_line_edit)
        self.btn_browse_perforce_dir = QtWidgets.QPushButton(self.frame_17)
        self.btn_browse_perforce_dir.setMinimumSize(QtCore.QSize(23, 0))
        self.btn_browse_perforce_dir.setMaximumSize(QtCore.QSize(23, 16777215))
        self.btn_browse_perforce_dir.setObjectName("btn_browse_perforce_dir")
        self.horizontalLayout_18.addWidget(self.btn_browse_perforce_dir)
        self.verticalLayout_5.addWidget(self.frame_17)
        self.frame_27 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_sync_resource = QtWidgets.QLabel(self.frame_27)
        self.label_sync_resource.setMinimumSize(QtCore.QSize(150, 30))
        self.label_sync_resource.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_sync_resource.setText("")
        self.label_sync_resource.setObjectName("label_sync_resource")
        self.horizontalLayout_27.addWidget(self.label_sync_resource)
        self.checkbox_sync_resource = QtWidgets.QCheckBox(self.frame_27)
        self.checkbox_sync_resource.setObjectName("checkbox_sync_resource")
        self.horizontalLayout_27.addWidget(self.checkbox_sync_resource)
        self.verticalLayout_5.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_sync_force = QtWidgets.QLabel(self.frame_28)
        self.label_sync_force.setMinimumSize(QtCore.QSize(150, 30))
        self.label_sync_force.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_sync_force.setText("")
        self.label_sync_force.setObjectName("label_sync_force")
        self.horizontalLayout_28.addWidget(self.label_sync_force)
        self.checkbox_sync_force = QtWidgets.QCheckBox(self.frame_28)
        self.checkbox_sync_force.setObjectName("checkbox_sync_force")
        self.horizontalLayout_28.addWidget(self.checkbox_sync_force)
        self.verticalLayout_5.addWidget(self.frame_28)
        self.frame_31 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_31.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_p4_charset_21 = QtWidgets.QLabel(self.frame_31)
        self.label_p4_charset_21.setMinimumSize(QtCore.QSize(150, 30))
        self.label_p4_charset_21.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_p4_charset_21.setText("")
        self.label_p4_charset_21.setObjectName("label_p4_charset_21")
        self.horizontalLayout_31.addWidget(self.label_p4_charset_21)
        self.checkbox_except_ddc = QtWidgets.QCheckBox(self.frame_31)
        self.checkbox_except_ddc.setObjectName("checkbox_except_ddc")
        self.horizontalLayout_31.addWidget(self.checkbox_except_ddc)
        self.verticalLayout_5.addWidget(self.frame_31)
        self.frame_32 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_p4_charset_22 = QtWidgets.QLabel(self.frame_32)
        self.label_p4_charset_22.setMinimumSize(QtCore.QSize(150, 30))
        self.label_p4_charset_22.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_p4_charset_22.setText("")
        self.label_p4_charset_22.setObjectName("label_p4_charset_22")
        self.horizontalLayout_32.addWidget(self.label_p4_charset_22)
        self.checkbox_except_intermediate = QtWidgets.QCheckBox(self.frame_32)
        self.checkbox_except_intermediate.setObjectName("checkbox_except_intermediate")
        self.horizontalLayout_32.addWidget(self.checkbox_except_intermediate)
        self.verticalLayout_5.addWidget(self.frame_32)

        self.frame_33 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_except_saved = QtWidgets.QLabel(self.frame_33)
        self.label_except_saved.setMinimumSize(QtCore.QSize(150, 30))
        self.label_except_saved.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_except_saved.setText("")
        self.label_except_saved.setObjectName("label_except_saved")
        self.horizontalLayout_33.addWidget(self.label_except_saved)
        self.checkbox_except_saved = QtWidgets.QCheckBox(self.frame_33)
        self.checkbox_except_saved.setObjectName("checkbox_except_saved")
        self.horizontalLayout_33.addWidget(self.checkbox_except_saved)
        self.verticalLayout_5.addWidget(self.frame_33)

        self.frame_34 = QtWidgets.QFrame(self.frame_general_2)
        self.frame_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_include_facs = QtWidgets.QLabel(self.frame_34)
        self.label_include_facs.setMinimumSize(QtCore.QSize(150, 30))
        self.label_include_facs.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_include_facs.setText("")
        self.label_include_facs.setObjectName("label_include_facs")
        self.horizontalLayout_34.addWidget(self.label_include_facs)
        self.checkbox_include_facs = QtWidgets.QCheckBox(self.frame_34)
        self.checkbox_include_facs.setObjectName("checkbox_include_facs")
        self.checkbox_include_facs.setText("FACS 폴더 싱크")
        self.horizontalLayout_34.addWidget(self.checkbox_include_facs)
        self.verticalLayout_5.addWidget(self.frame_34)

        self.verticalLayout_8.addWidget(self.frame_general_2)
        self.settings_tab_widget.addTab(self.tab_general_option, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_settings.setObjectName("tab_settings")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_settings)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_perforce = QtWidgets.QFrame(self.tab_settings)
        self.frame_perforce.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_perforce.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_perforce.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_perforce.setObjectName("frame_perforce")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_perforce)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_19 = QtWidgets.QFrame(self.frame_perforce)
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_34 = QtWidgets.QFrame(self.frame_19)
        self.frame_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_p4_server = QtWidgets.QLabel(self.frame_34)
        self.label_p4_server.setMinimumSize(QtCore.QSize(80, 50))
        self.label_p4_server.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_p4_server.setObjectName("label_p4_server")
        self.label_p4_server.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_10.addWidget(self.label_p4_server)
        self.le_p4_server = QtWidgets.QLineEdit(self.frame_34)
        self.le_p4_server.setMinimumSize(QtCore.QSize(0, 0))
        self.le_p4_server.setObjectName("le_p4_server")
        self.horizontalLayout_10.addWidget(self.le_p4_server)
        self.verticalLayout_7.addWidget(self.frame_34)
        self.frame_35 = QtWidgets.QFrame(self.frame_19)
        self.frame_35.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_p4_user = QtWidgets.QLabel(self.frame_35)
        self.label_p4_user.setMinimumSize(QtCore.QSize(80, 50))
        self.label_p4_user.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_p4_user.setObjectName("label_p4_user")
        self.label_p4_user.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_19.addWidget(self.label_p4_user)
        self.le_p4_user = QtWidgets.QLineEdit(self.frame_35)
        self.le_p4_user.setMinimumSize(QtCore.QSize(0, 0))
        self.le_p4_user.setObjectName("le_p4_user")
        self.horizontalLayout_19.addWidget(self.le_p4_user)
        self.verticalLayout_7.addWidget(self.frame_35)
        self.frame_36 = QtWidgets.QFrame(self.frame_19)
        self.frame_36.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_p4_password = QtWidgets.QLabel(self.frame_36)
        self.label_p4_password.setMinimumSize(QtCore.QSize(80, 50))
        self.label_p4_password.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_p4_password.setObjectName("label_p4_password")
        self.label_p4_password.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_34.addWidget(self.label_p4_password)
        self.le_p4_password = QtWidgets.QLineEdit(self.frame_36)
        self.le_p4_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_p4_password.setMinimumSize(QtCore.QSize(0, 0))
        self.le_p4_password.setObjectName("le_p4_password")
        self.horizontalLayout_34.addWidget(self.le_p4_password)
        self.verticalLayout_7.addWidget(self.frame_36)
        self.frame_37 = QtWidgets.QFrame(self.frame_19)
        self.frame_37.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_37)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_p4_client = QtWidgets.QLabel(self.frame_37)
        self.label_p4_client.setMinimumSize(QtCore.QSize(80, 50))
        self.label_p4_client.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_p4_client.setObjectName("label_p4_client")
        self.label_p4_client.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_35.addWidget(self.label_p4_client)
        self.combobox_p4_client = QtWidgets.QComboBox(self.frame_37)
        self.combobox_p4_client.setObjectName("combobox_p4_client")
        self.horizontalLayout_35.addWidget(self.combobox_p4_client)
        self.verticalLayout_7.addWidget(self.frame_37)

        self.frame_38 = QtWidgets.QFrame(self.frame_19)
        self.frame_38.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_p4_charset = QtWidgets.QLabel(self.frame_38)
        self.label_p4_charset.setMinimumSize(QtCore.QSize(80, 50))
        self.label_p4_charset.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_p4_charset.setObjectName("label_p4_charset")
        self.label_p4_charset.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_36.addWidget(self.label_p4_charset)
        self.combobox_p4_charset = QtWidgets.QComboBox(self.frame_38)
        self.combobox_p4_charset.setObjectName("combobox_p4_charset")
        self.horizontalLayout_36.addWidget(self.combobox_p4_charset)
        self.verticalLayout_7.addWidget(self.frame_38)

        button_frame = QtWidgets.QFrame(self.frame_19)
        button_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        button_frame.setObjectName("button_frame")
        button_layout = QtWidgets.QHBoxLayout(button_frame)
        button_layout.setSpacing(0)
        button_layout.setContentsMargins(10, 0, 0, 0)
        button_layout.setObjectName("button_layout")
        self.add_env_button = QtWidgets.QPushButton("환경변수 추가")
        self.add_env_button.setObjectName("add_env_button")
        self.add_env_button.setMinimumSize(QtCore.QSize(100, 30))
        # button_layout.addWidget(self.add_env_button)
        spacer_item = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        button_layout.addItem(spacer_item)
        self.save_button = QtWidgets.QPushButton("저장")
        self.save_button.setObjectName("save_button")
        self.save_button.setMinimumSize(QtCore.QSize(100, 30))
        button_layout.addWidget(self.save_button)
        self.verticalLayout_7.addWidget(button_frame)

        self.verticalLayout_6.addWidget(self.frame_19)
        self.verticalLayout_9.addWidget(self.frame_perforce)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacer_item)
        self.settings_tab_widget.addTab(self.tab_settings, "")
        self.verticalLayout.addWidget(self.settings_tab_widget)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        self.retranslate_ui()
        self.settings_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.connect_signals()

    def retranslate_ui(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("central_widget", "Form", None, -1))
        self.label_engine_root.setText(
            QtWidgets.QApplication.translate("central_widget", "Engine Root Directory ", None, -1)
        )
        self.btn_browse_engine_dir.setText(QtWidgets.QApplication.translate("central_widget", "...", None, -1))
        self.checkbox_enable_dx12.setText(
            QtWidgets.QApplication.translate("central_widget", "에디터 실행시 DX12, Raytracing 옵션 추가", None, -1)
        )
        self.label_p4_exe.setText(QtWidgets.QApplication.translate("central_widget", "P4.exe 파일 ", None, -1))
        self.p4_path_line_edit.setText(
            QtWidgets.QApplication.translate("central_widget", "C:\\Program Files\\Perforce\\p4.exe", None, -1)
        )
        self.btn_browse_perforce_dir.setText(QtWidgets.QApplication.translate("central_widget", "...", None, -1))
        self.checkbox_sync_resource.setText(
            QtWidgets.QApplication.translate("central_widget", "Resource 폴더도 함께 sync", None, -1)
        )
        self.checkbox_sync_force.setText(
            QtWidgets.QApplication.translate("central_widget", "싱크할때 force 옵션 추가", None, -1))
        # self.checkbox_env_var.setText(QtWidgets.QApplication.translate("central_widget", "환경 변수 자동 설정", None, -1))
        # self.checkbox_editor_p4.setText(QtWidgets.QApplication.translate("central_widget", "UE4 에디터 퍼포스 자동 설정", None, -1))
        self.checkbox_except_ddc.setText(
            QtWidgets.QApplication.translate("central_widget", "DerivedDataCache 싱크 제외", None, -1))
        self.checkbox_except_intermediate.setText(
            QtWidgets.QApplication.translate("central_widget", "Intermediate 싱크 제외", None, -1))
        self.checkbox_except_saved.setText(QtWidgets.QApplication.translate("central_widget", "Saved 싱크 제외", None, -1))
        self.settings_tab_widget.setTabText(self.settings_tab_widget.indexOf(self.tab_general_option),
                                            QtWidgets.QApplication.translate("central_widget", "General", None, -1))
        self.label_p4_server.setText(QtWidgets.QApplication.translate("central_widget", "P4 Server ", None, -1))
        self.label_p4_user.setText(QtWidgets.QApplication.translate("central_widget", "P4 User ", None, -1))
        self.label_p4_password.setText(QtWidgets.QApplication.translate("central_widget", "P4 Password ", None, -1))
        self.label_p4_client.setText(QtWidgets.QApplication.translate("central_widget", "P4 Client ", None, -1))
        self.label_p4_charset.setText(QtWidgets.QApplication.translate("central_widget", "P4 Charset ", None, -1))
        self.settings_tab_widget.setTabText(self.settings_tab_widget.indexOf(self.tab_settings),
                                            QtWidgets.QApplication.translate("central_widget", "Perforce", None, -1))

    def connect_signals(self):
        self.btn_browse_engine_dir.clicked.connect(self.browse_dir)
        self.btn_browse_perforce_dir.clicked.connect(self.browse_dir)
        self.save_button.clicked.connect(self.save_settings)
        self.le_p4_password.editingFinished.connect(self.password_edited)

    def set_ui(self, data):
        settings_data = data["Settings"]
        p4exe_path = settings_data.get("P4exe", r"C:\Program Files\Perforce\p4.exe")
        self.engine_path_line_edit.setText(settings_data["EngineRoot"])
        self.checkbox_enable_dx12.setChecked(settings_data.get("EnableDx12", False))
        self.p4_path_line_edit.setText(p4exe_path)
        self.checkbox_sync_resource.setChecked(settings_data.get("SyncResource", True))
        self.checkbox_sync_force.setChecked(settings_data.get("ForceSync", True))
        self.checkbox_except_ddc.setChecked(settings_data.get("ExceptDDC", True))
        self.checkbox_except_intermediate.setChecked(settings_data.get("ExceptIntermediate", True))
        self.checkbox_except_saved.setChecked(settings_data.get("ExceptSaved", True))
        self.checkbox_include_facs.setChecked(settings_data.get("IncludeFACS", True))

        server = self.parent.p4cmd.p4.port
        user = self.parent.p4cmd.p4.user
        password = self.parent.p4cmd.p4.password
        client = self.parent.p4cmd.p4.client
        clients = self.get_clients(user, password)
        charset = self.parent.p4cmd.p4.charset

        if server:
            self.le_p4_server.setText(str(server))
            self.le_p4_user.setText(str(user))
            self.le_p4_password.setText(str(password))
            self.combobox_p4_client.addItems(clients)
            self.combobox_p4_client.setCurrentText(client)
            self.combobox_p4_charset.addItems(["utf8", "none"])
            self.combobox_p4_charset.setCurrentText(charset)

    def password_edited(self):
        self.combobox_p4_client.clear()
        user = self.le_p4_user.text()
        password = self.le_p4_password.text()
        clients = self.get_clients(user, password)
        if clients:
            self.combobox_p4_client.addItems(clients)

    def set_environ(self, path):
        path_string = os.environ["path"]
        if path not in path_string.split(";"):
            path_string += ";" + path
        os.environ["path"] = path_string

    def get_settings(self):
        settings = config.CONFIG["Settings"]
        settings["EngineRoot"] = self.engine_path_line_edit.text()
        settings["EnableDx12"] = self.checkbox_enable_dx12.isChecked()
        settings["P4exe"] = self.p4_path_line_edit.text()
        settings["SyncResource"] = self.checkbox_sync_resource.isChecked()
        settings["ForceSync"] = self.checkbox_sync_force.isChecked()
        settings["ExceptDDC"] = self.checkbox_except_ddc.isChecked()
        settings["ExceptIntermediate"] = self.checkbox_except_intermediate.isChecked()
        settings["ExceptSaved"] = self.checkbox_except_saved.isChecked()
        settings["IncludeFACS"] = self.checkbox_include_facs.isChecked()
        return settings

    def browse_dir(self):
        sender = self.sender()
        if sender.objectName() == "btn_browse_engine_dir":
            path = QtWidgets.QFileDialog.getExistingDirectory(self, '폴더 선택', "", QtWidgets.QFileDialog.ShowDirsOnly)
            path = path.replace("/", "\\")
            self.engine_path_line_edit.setText(str(path))
        else:
            path = QtWidgets.QFileDialog.getOpenFileName(self, '파일 선택', "", "p4.exe")
            if path:
                path = path[0].replace("/", "\\")
                self.p4_path_line_edit.setText(str(path))

    def get_clients(self, user, password):
        clients = self.parent.p4cmd.get_workspaces(user, password)
        if not clients:
            QtWidgets.QMessageBox.critical(self, "경고", "로그인 정보 확인")
        return clients

    def save_settings(self):
        server = self.le_p4_server.text()
        user = self.le_p4_user.text()
        password = self.le_p4_password.text()
        client = self.combobox_p4_client.currentText()
        charset = self.combobox_p4_charset.currentText()

        subprocess.call(["p4", "set", f"P4PORT={server}"])
        subprocess.call(["p4", "set", f"P4USER={user}"])
        subprocess.call(["p4", "set", f"P4PASSWD={password}"])
        subprocess.call(["p4", "set", f"P4CLIENT={client}"])
        subprocess.call(["p4", "set", f"P4CHARSET={charset}"])

