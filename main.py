from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
import random 


kv="""
UI:
<UI>:        
    Label:
        id: hello
        text: "hello"
        size_hint: .1,.05
        pos_hint: {"x":.45,"y":.475}
    Label:
        id: print
        text: "#"
        size_hint: .1,.05
        pos_hint: {"x":.45,"y":.9}
    Label:
        id: item
        text: "#"
        size_hint: .1,.05
        pos_hint: {"x":.45,"y":.8}
    Button:
        text: "left"
        size_hint: .3,.1
        pos_hint: {"x":.05,"y":.1}
        on_press: root.left()
        
    Button:
        text: "right"
        size_hint: .3,.1
        pos_hint: {"x":.65,"y":.1}
        on_press: root.right()
        
    Button:
        text: "up"
        size_hint: .3,.1
        pos_hint: {"x":.35,"y":.2} 
        on_press: root.up()
        
    Button:
        text: "down"
        size_hint: .3,.1
        pos_hint: {"x":.35,"y":.0}
        on_press: root.down()
        
        
"""

class UI(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.item, .1/60)
        Clock.schedule_interval(self.move, 1.0 / 60.0)            
        
        self.top_speed = 7      
        #---x-axis---
        self.pos_x = .45
        self.speed_x = self.top_speed/Window.width        
        self.move_left = False
        self.move_right = False        
        #---y-axis---
        self.speed_y = self.top_speed/Window.height
        self.pos_y = .475        
        self.move_up = False
        self.move_down = False
        self.letter = ""
        
        self.pos_xi = 0
        self.pos_yi = 0
        self.n = 0
        
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
              
    def show(self, message):
            self.ids.print.text = message      
    #---x-axis---            
    def right(self):         
        self.move_left = False
        self.move_right = True
        self.move_up = False
        self.move_down = False     
    def left(self):                      
        self.move_left = True
        self.move_right = False
        self.move_up = False
        self.move_down = False                                    
    #---y-axis---  
    def up(self): 
        self.move_left = False
        self.move_right = False
        self.move_up = True
        self.move_down = False                    
    def down(self):             
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = True      
                   
    def item(self,dt):
        self.letter = random.choice(self.letters)
        self.pos_xi = random.uniform(0,1)
        self.pos_yi = random.uniform(0.3,1)
        self.ids.item.text = self.letter       
        
        #self.ids.item.pos_hint = {"x": self.pos_xi,"y": self.pos_yi}  
        self.ids.item.pos_hint = {"x":self.pos_x,"y":self.pos_y}  
                  
    def move (self, dt):    
                                     
        if self.move_right:
            self.pos_x += self.speed_x                             
        if self.move_left:
            self.pos_x -= self.speed_x                         
                                          
        if self.move_up:
            self.pos_y += self.speed_y
        if self.move_down:
            self.pos_y -= self.speed_y                 
                                         
        if self.pos_x > 1:
            self.pos_x = -.1
        elif self.pos_x < -.1:
            self.pos_x = 1 
        if self.pos_y > 1:
            self.pos_y = -.1
        elif self.pos_y < -.1:
            self.pos_y = 1          
                                                                                                       
        #self.show(str(f"{self.speed_x} \n {self.speed_y}"))
        
        distance = ((self.pos_x - self.pos_xi)**2 + (self.pos_y - self.pos_yi)**2)**.5
        if distance < .02:
            self.item(0)
            self.n += 1
        self.show(str(self.n))
        self.ids.hello.pos_hint = {"x":self.pos_x,"y":self.pos_y}  
                                                                                                        
                                                                                                        
class Inertia(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    Inertia().run()
