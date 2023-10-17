#main.py
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MainWidget(GridLayout): 
    pass


#class Ui(ScreenManager):
 #   pass
    #def build(self): Day 67 
        # Setting theme to my favorite theme
        #self.theme_cls.primary_palette = "DeepPurple"
        #self.audio_files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]
    
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_file("styles.kv")

        #return Ui()
        return MainWidget()

if __name__ == '__main__':
    MainApp().run()