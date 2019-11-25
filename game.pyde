# this is a modified version of the game "NS-SHAFT"
import os
path = os.getcwd+'/'


class Player:
    def __init__(self,x,y,h): # h: health
        self.x = x
        self.y = y
        self.h = h
    
    def gravity(self)
    
    def jump(self)
    
    def fall(self)
    
    def lose_health(self,h,loss)
    
    def gain_health(self,h,gain)
    
    def die(self)
    
    def update(self)
    
    def display(self)
    

class Platform:
    def __init__(self,x,y,r,img):
        self.x = x
        self.y = y
        self.r = r
        self.img = loadImage(path+'images/'+img)
    
    def update(self)
    
    def display(self)
    

class Ord(Platform):
    def __init__(self,x,y,r,img):
        Platform.__init__(self,x,y,r,img)

class Fake(Platform):
    def __init__(self,x,y,r,img):
    Platform.__init__(self,x,y,r,img)

class Spiky(Platform):
    def __init__(self,x,y,r,img):
    Platform.__init__(self,x,y,r,img)
    
class Flip(Platform):
    def __init__(self,x,y,r,img):
    Platform.__init__(self,x,y,r,img)

class Conveyor(Platform):
    def __init__(self,x,y,r,img,dir):
    Platform.__init__(self,x,y,r,img)
    self.dir = dir

class Obstacles:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = loadImage(path+'images/'+img)

class Supplements:
    def __init__(self,x,y,h,img):
        self.x = x
        self.y = y
        self.h = h
        self.img = loadImage(path+'images/'+img)

Class Top_spike:
    def init(self,x,y,img):
        self.x = 0
        self.y = 0
        img = loadImage(path+'images/top_spike')
        

class Background:
    def __init__(self,img):
        self.img = loadImage(path+'images/'+img)

class Game:
    def __init__(self,p,b):
        self.p = p
        self.b = b
    
    def display(self):
        #print the background
        #print the player and the platforms
    
    def update(self):
        



def setup():
    size(600,800)

def draw():
    g.display
    
