#Starting from zero
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp

# Designate your kv file
Builder.load_file('main.kv')

class MyLayout(Widget):
    pass

class MyApp(MDApp):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    MyApp().run()
