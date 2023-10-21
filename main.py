#Starting from zero
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager


#day focused in the Uix design

class Ui(ScreenManager):
    pass

class cls(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file('cls.kv')
        return Ui()
    
if __name__ == '__main__':
    cls().run()
