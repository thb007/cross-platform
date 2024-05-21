from kivy.app import App
from kivy.uix.screenmanager import Screen

class UI(Screen):
    def add_item(self): #นำค่าที่พิมพ์ผ่านช่อง textinput ไปเพิ่มใน spinner
        self.ids.spin1.values.append(self.ids.t1.text)


class SpinnerApp(App): #class หลัก
    def build(self):
        return UI()

if __name__ == "__main__":
    SpinnerApp().run()