from datetime import datetime

from backend.Logic.LogicManager import *
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker
from kivy.config import Config

from frontend.gui_strings import alarm_string, screen_helper
from frontend.screens.AlarmActiveScreen import *
from frontend.screens.AlarmFormScreen import *
from frontend.screens.DismissSpeechScreen import *
from frontend.screens.MainScreen import *
from frontend.screens.EnterScreen import *
from frontend.screens.TODOScreen.TODOScreen import *
from frontend.screens.TODOScreen.TODOFormScreen import *

# setting up default window size
#Window.size = ('fullscreen')
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1000')
Config.write()

# Create a screen manager
sm = ScreenManager()
sm.add_widget(EnterScreen(name="enter"))
sm.add_widget(MainScreen(name="main"))
sm.add_widget(AlarmFormScreen(name="alarm_form"))
sm.add_widget(AlarmActiveScreen(name="alarm_active"))
sm.add_widget(DismissSpeechScreen(name="dismiss_speech"))
sm.add_widget(TODOScreen(name="todo"))
sm.add_widget(TODOFormScreen(name="todo_form"))


class AlarmApp(MDApp):
    """
    This class is the entry-point of the application.
    It is responsible for initialization, and displaying the Main Screen.
    """

    def __init__(self, args, **kwargs):
        super(MDApp, self).__init__(**kwargs)
        self.args = args

    def build(self):
        self.icon = "./assets/alarm_clock_icon.png"
        self.title = "Wake me A.I"
        # sets color theme
        self.theme_cls.primary_palette = 'Purple'
        # create the main screen Widget
        screen_manager = Builder.load_string(screen_helper)
        main_screen = screen_manager.screens[1]
        logic_manger = LogicManager(self.args, main_screen)
        main_screen.set_logic_manager(logic_manger)
        return screen_manager
