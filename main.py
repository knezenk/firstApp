import os
from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.core.window import Window


class LiveApp(MDApp, App):
    DEBUG = "DEBUG"

    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv"),
    }

    CLASSES = {
        'MainScreenManager': "screens.screenmanager",
        'LoginScreen': "screens.login_screen.loginscreen",
    }

    AUTORELOADER_PATHS = [
         (".", {"recursive": False}),
    ]

    RAISE_ERROR = True


    def build_app(self):
        Window.size = [350, 560]
        return Factory.MainScreenManager()


LiveApp().run()
