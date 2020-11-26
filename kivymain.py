import PicInPic2 as PiP
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class  MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)

        self.cols=2

        self.add_widget(Label(text="Carrier "))

        self.carrier=TextInput(multiline=False)
        self.add_widget(self.carrier)

        self.add_widget(Label(text="Payload "))
        
        self.payload=TextInput(multiline=False)
        self.add_widget(self.payload)

        self.add_widget(Label(text="Output "))
        
        self.out=TextInput(multiline=False)
        self.add_widget(self.out)

        self.submit=Button(text="Submit",font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self,instance):
        carrier=self.carrier.text
        payload=self.payload.text
        out=self.out.text
        PiP.merge(carrier,payload,out)
        self.add_widget(Label(text="Merged"))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__=='__main__':
    MyApp().run()