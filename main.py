#main.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

class Ui(ScreenManager):
    pass
    #def build(self): Day 66 freeday
        # Setting theme to my favorite theme
        #self.theme_cls.primary_palette = "DeepPurple"
        #self.audio_files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]
    
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_file("main.kv")

        return Ui()

if __name__ == '__main__':
    MainApp().run()