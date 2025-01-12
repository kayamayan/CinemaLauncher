# encoding:utf-8

class VtLauncherSettings:

    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 180
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 200  # 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    QPushButton {
         background-position: center;
         background-repeat: no-reperat;
         border: none;
         border-left: 10px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(85, 170, 255, 255), stop:0.5 rgba(85, 170, 255, 0));
         background-color: rgb(36, 36, 36);
     }
     QPushButton:hover {
         background-color: rgb(33, 37, 43);
     }
     QPushButton:pressed {    
         background-color: rgb(85, 170, 255);
     }
    """

    ADMINS = {
        "172.18.93.232": "정경헌"
    }

    def __init__(self):
        self.perforce_settings = {}
        self.general_setting = {}
