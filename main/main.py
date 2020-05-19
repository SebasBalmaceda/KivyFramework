import kivy
kivy.require("1.8.4")
from kivy.app import App
from kivy.uix.button import Button

#las widget siempre son clases
class App(App):  #Nombre de la aplicacion ya que tiene que llevar el nombre de kv
    def build(self):   #funcion para correr la app
        return Button(text='Hello World')


App().run()                    #necesario para correr la app


