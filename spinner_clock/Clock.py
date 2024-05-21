from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.clock import Clock

class UI(ScreenManager):
    pass

class Logo_page(Screen): #หน้า1
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.go_to_screen,3)

    def go_to_screen(self,sec):
        self.manager.current = "Page1"

class Page1(Screen): #หน้า2
    count = 0
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.update_lable,2)

    def update_lable(self,num):
        self.count+=1
        self.ids.lbl_count.text = str(self.count)
        

class ClockApp(App):
    def build(self):
        return UI()
    
if __name__ == "__main__":
    ClockApp().run()