#не забудь импортировать необходимые элементы!
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class Scrbtn(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation='vertical', padding=8, spacing=8)
        h1 = BoxLayout()
        txt = Label(text= 'Choose a screen')
        v1.add_widget(Scrbtn(self, direction='down', goal='first', text='1'))
        v1.add_widget(Scrbtn(self, direction='left', goal='second', text='2'))
        v1.add_widget(Scrbtn(self, direction='up', goal='third', text='3'))
        v1.add_widget(Scrbtn(self, direction='right', goal='fourth', text='4'))

        h1.add_widget(txt)
        h1.add_widget(v1)
        self.add_widget(h1)

class MyApp(App):
    def build(self):
        txt = Label(text='p')
        btn = Button(text='Press')
  
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

MyApp().run() 