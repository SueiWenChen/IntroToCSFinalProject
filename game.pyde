# this is a modified version of the game "NS-SHAFT"
import os, tkinter
path = os.getcwd+'/'

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.game_frame = tkiner.Frame(self.main_window)
        self.score_frame = tkiner.Frame(self.main_window)
        self.health_frame = tkiner.Frame(self.main_window)
        
        
        thinter.mainloop()


class Player:
    def __init__(self,x,y,r,dir,h): # h: health
        self.x = x
        self.y = y
        self.r = r
        self.dir = dir
        self.h = h
    
    def gravity(self): # if the player is on a platform, stop falling; otherwise fall

        if self.y+self.r >= self.g: # when the bottom of the image is on or below the ground
            self.vy = 0
        else: # when above the ground
            self.vy += 0.4 #decrement of height
            if self.y + self.r + self.vy > self.g: # if new height is below the ground
                 self.vy = self.g - (self.y+self.r) # g - (y+r) is the difference 
        
        for p in g.platforms:  # check every platform in the list of platforms
            if self.y + self.r <= p.y and self.x+self.r >= p.x and self.x-self.r <= p.x+p.w:
                self.g = p.y
                break
            self.g = g.g
            
    def move(self):
        if self.x - self.r <= player.x <= self.x + self.r and player.y == self.y - self.r:
            def update(self):
            self.gravity()
        
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.direction = -1
        elif self.keyHandler[RIGHT]:
            self.vx = 8
            self.direction = 1
        else:
            self.vx = 0
            
        if self.keyHandler[UP] and self.y + self.r == self.g:
            self.jumpSound.rewind()
            self.jumpSound.play()
            self.vy = -15
            
        if self.x - self.r < 0:
            self.x = self.r          #mario is not allowed to go beyond the left window
        
        self.x += self.vx
        self.y += self.vy   
   
    def spring(self): # when hitting a spring 
    
    def carry(self,conveyor):
        if conveyor.x - conveyor.r <= self.x <= conveyor.x + conveyor.r:
           self.x += conveyor.dir[self.dir]*conveyor.speed
    
    def lose_health(self,h,loss):   # h <= 12, deduction = 5/time
    
    def gain_health(self,h,gain)
    
    def die(self)
    
    def update(self):
        self.gravity()
    
    def display(self)
    

class Platform:
    def __init__(self,x,y,r,img):
        self.x = x
        self.y = y
        self.r = r
        self.img = loadImage(path+'images/'+img)
    
    def update(self):
        self.y -= g.v
    
    def display(self):
        image(img,#x,#y,#width,#height)
    

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
    
    def flip(self):
        if player.y # is within the height range of such a platform:
            player.y += # falling speed

class Conveyor(Platform):
    def __init__(self,x,y,r,img,dir,speed): # dir = {LEFT:-1, RIGHT;+1}
        Platform.__init__(self,x,y,r,img)
        self.dir = dir
        self.speed = speed
    

        

class Sping(Platform):
    def __init__(self,x,y,r,img):
        Platform.__init__(self,x,y,r,img)
    



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
    
    def eaten(self):
        if #same location:
            del

Class Top_spike:
    def init(self,x,y,img):
        self.x = 0
        self.y = 0
        img = loadImage(path+'images/top_spike')
    
    def hit(self):
        # deduct life
        # version 1: if originally on a platform, drop the player down
        # version 2: if the player gets sandwiched he loses

class HealthBar:
    def __init__(self,h):
        self.h = h
    
    def display(self): # h <= 12
        strokeWeight(5)
        stroke(0)
        fill(255,255,0)
        for i in range(h):
            rect(10,20)
        fill(255)
        for i in range(12-h):
            rect(10,20)        
            
        

class Background:
    def __init__(self,img):
        self.img = loadImage(path+'images/'+img)

class Game:
    def __init__(self,y,v,platform,bgd):
        self.y = y # the 'height' of the game
        self.v = v # velocity of the downward movement
        self.platform = platform
        self.bgd = bgd
        self.score = self.y//800
    
    def display(self):
        #print the background
        #print the player and the platforms
    
    def update(self):
        
        

# put the game in the frame, and display the frame in the window

# actually we can use rectangles as platforms; in this way animation may be easier


my_gui = myGUI()
    
