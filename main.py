from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from  kivy.uix.boxlayout import BoxLayout


class Demo(GridLayout):
    pass
    


class AppPjApp(App):
    def build(self):
        #layout = Demo()
        #layout = BoxLayout(orientation='vertical')
        #
        #layout.add_widget(Label(text='CADASTRO DE MEMBROS', height = 40, size_hint_y=None, pos_hint_y = None))        
        #layout.add_widget(TextInput(text='Digite o Nome do Membro', height = 40, size_hint_y=None, pos_hint_y = None))        
        #layout.add_widget(TextInput(text='Digite o E-Mail do Membro', height = 40, size_hint_y=None, pos_hint_y = None))        
        #layout.add_widget(TextInput(text='Digite o Telefone do Membro', height = 40, size_hint_y=None, pos_hint_y = None))
        #layout.add_widget(Button(text='blablabla', center_x = layout.center_x, height = 40, size_hint_y=None, pos_hint_y = None))
        
        return Demo()
    
if __name__ == '__main__':
    AppPjApp().run()