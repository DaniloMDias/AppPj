from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty

from kivy.vector import Vector
from kivy.clock import Clock

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


class Login(Screen):
    pass

class Apresentacao(Screen):
    pass

class Cadastro(Screen):
    pass

class Contatos(Screen):
    pass

class Manager(ScreenManager):
    pass

    


class AppPjApp(App):
    def build(self):
        
        
        return Manager()
    
if __name__ == '__main__':
    AppPjApp().run()