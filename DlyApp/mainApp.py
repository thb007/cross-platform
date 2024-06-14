from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):  # หน้า 2
    def check_inputs(self):
        id_number1 = self.ids.TNP1.text
        id_number2 = self.ids.TNP2.text
        phone_number = self.ids.phone_input.text
        if len(id_number1) == 13 and len(id_number2) == 13 and len(phone_number) == 10:
            self.ids.btn_regis.text = "พร้อมบันทึกข้อมูล"
        else:
            self.ids.btn_regis.text = "ไม่พร้อมบันทึกข้อมูล"

class MainScreen(Screen):  # หน้าจอ 1
    pass

class UI(ScreenManager):  # ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class mainApp(App):
    def build(self):
        return UI()

if __name__ == "__main__":   
    mainApp().run()
