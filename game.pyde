# this is a modified version of the game "NS-SHAFT"
import os, tkinter
path = os.getcwd+'/'

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.game_frame = tkiner.Frame(self.main_window)
        self.score_frame = tkiner.Frame(self.main_window)
        self.health_frame = tkiner.Frame(self.main_window)
        # press 's' to start
        # press 'p' to pause and press again to resume
        
        thinter.mainloop()

class Platform:
    def __init__(self,x,y,img): # (x,y): upper-left corner, w = width
        self.x = x
        self.y = y
        self.w = w
        # self.img = loadImage(path+'images/'+img)
    
    def update(self):
        self.y -= g.v
    
    def display(self):
        image(img,#x,#y,#width,#height)
    
class Ord(Platform):
    def __init__(self,x,y,img,num): # num is for indentification of platform types
        Platform.__init__(self,x,y,img)
        self.num = 0

class Fake(Platform):
    def __init__(self,x,y,img,num):
        Platform.__init__(self,x,y,img)
        self.num = 1

class Spiky(Platform):
    def __init__(self,x,y,img,num):
        Platform.__init__(self,x,y,img)
        self.num = 2
    
class Flip(Platform):
    def __init__(self,x,y,img,num):
        Platform.__init__(self,x,y,img)
        self.num = 3
    def display(self):
        # we need images of the flipping

class Conveyor(Platform):
    def __init__(self,x,y,r,img,v,num):
        Platform.__init__(self,x,y,img)
        self.num = 4
        self.v = v # +5: right; -5: left
    def display(self):
        # we can potentially add animation to this
    
class Spring(Platform):
    def __init__(self,x,y,r,img,num):
        Platform.__init__(self,x,y,img)
        self.num = 5
    def display(self):
        # we need images of the elastic movement

class Obstacles:
    def __init__(self,x,y,img): # (x,y): upper-left corner
        self.x = x
        self.y = y
        self.w = w # width
        self.h = h # height
        self.img = loadImage(path+'images/'+img)

class Supplements:
    def __init__(self,x,y,l,w,img): # (x,y): upper-left corner
        self.x = x
        self.y = y
        self.h = h # height
        self.w = w # width
        self.img = loadImage(path+'images/'+img)

class Top_spike:
    def init(self,x,y,img):
        self.x = 0
        self.y = 0
        img = loadImage(path+'images/top_spike')

class HealthBar:
    def __init__(self):
        self.h = 12
    
    # def display(self): # h <= 12 Q: how to display in a specific frame?
    #     strokeWeight(5)
    #     stroke(0)
    #     fill(255,255,0)
    #     for i in range(p.h):
    #         rect(10,20)
    #     fill(255)
    #     for i in range(12-p.h):
    #         rect(10,20)        
            
class Player:
    def __init__(self,x,y): # (x,y): center, h: health
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.v_fall = 0
        self.dvx = 0 # velocity of conveyor belts
        self.fv = 5 # velocity of flipping down
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
        self.h = 12
        self.number = 0 # the type of platform on which the player stands
        self.landed = 0 # 1 means landed and updates are yet to be made; 0 otherwise
        self.flip_range = [] # the range within which the player flips

    def gravity(self): # if the player is on a proper platform, stop falling; otherwise fall
        on_a_platform = False
        for p in g.platforms:  # check every platform in the list of platforms
            if p.num != 1: # not a deceptive one
                if self.y + self.r == p.y and p.x - p.w <= self.x <= p.x+p.w: #if on a platform
                    self.y = p.y - self.r
                    self.v_fall = 0
                    on_a_platform = True
                    self.number = p.num # keep track of the type of platform the player is on
                    if p.num == 3: # if on a flip one 
                        self.flip_range = [p.y,p.y+20] # fall at a certain speed within this range; 20 = height 
                        self.v_fall = 5
                    if p.num == 4: # if on a belt, keep track of the velocity
                        self.dvx = p.v
                    break
                elif self.y+self.r<p.y and self.y+self.r+self.v_fall+0.4>=p.y-g.v_down and p.x-p.w<=self.x<=p.x+p.w: 
                # if during an update the player hits a platform
                    self.v_fall = p.y - (self.y+self.r) - g.v_down # land on a platform
                    self.landed = 1
                    on_a_platform = True
                    break
            if p.num == 1 and self.y+self.r<p.y and self.y+self.r+self.v_fall+0.4>=p.y-g.v_down and p.x-p.w<=self.x<=p.x+p.w: 
                del p # del the fake platform once the player reaches it
                # sound effect of disappearing
        if not on_a_platform:
            self.v_fall += 0.4
        
    def effects(self): 
        if self.number == 5: # when hitting a spring
            self.v_fall = -15
        
        if self.number == 3: # when hitting a flip platform
            if self.flip_range[0]<self.y<=self.flip_range[1]:
                self.v_fall = self.fv

        if self.number == 4: # when on a conveyor
           self.vx += self.dvx
    
    def new_health(self): 
        if self.number == 2 or self.y < self.r and self.landed == 1:  # deduction
            self.h -= 5
            self.landed = 0  # deduction done        
        
        if self.h < 12 and self.number != 2 and self.landed == 1: # increase
            self.h += 1
            self.landed = 0  # increase done    
        for s in g.supplements: # replenishment
            if s.x <= self.x <= s.x + s.w and s.y <= self.y <= s.y + s.h:
                self.h = 12
                del s
                break

    def die(self):
        if self.h <= 0 or self.y <= 0:
            return true

    def update(self):
        if not self.die():
            self.new_health()
            H.h = self.h        
            
            if self.keyHandler[LEFT]:
                self.vx = -10
            elif self.keyHandler[RIGHT]:
                self.vx = 10
            else:
                self.vx = 0
                
            if self.keyHandler[UP] and on_a_platform==True:
                # self.jumpSound.rewind()
                # self.jumpSound.play()
                self.v_fall = -15
           
            self.gravity()
            self.effects() # update according to the type of platform
    
            # move
            self.x += self.vx
            self.y += self.v_fall       
            # the player is not allowed to go outside the view
            if self.x - self.r < 0:
                self.x = self.r 
            if self.x + self.r > 800:
                self.x = 800 - self.r
            # # the player is cannot run into obstacles or platforms
            # # not sure of this block of code yet
            # for o in g.obstacles:
            #     if self.keyHandler[LEFT] and o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h:
            #         self.x = o.x+o.w
            #     if self.keyHandler[RIGHT] and o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h:
            #         self.x = o.x
            #     if o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h and self.v_fall>0:
                    

            self.landed = 0 # updates are done
        
        if self.die():
            # sound effect
            # display a pop-up window showing 'game over' and 'press [something] to restart'
            # restart the game
            
    
    def display(self)    

class Background:
    def __init__(self,img):
        self.img = loadImage(path+'images/'+img)

class Game:
    def __init__(self,y,v_down,delta_v_down,platform,bgd):
        self.y = y # the 'height' of the game
        self.v_down = 100 # velocity of the downward movement
        self.delta_v_down = 1/1000 
        self.platform = platform
        self.bgd = bgd
        self.score = self.y//800
        # instantiate relevant objects here
    
    def display(self):
        #print the background
        #print the player and the platforms
        
    
    def update(self):
        # move up all the objects (potentially except the player) and the scope appears to move down 
        for p in g.platforms:
            p.y -= self.v_down
        for o in g.obstacles:
            o.y -= self.v_down
        for s in g.supplements:
            s.y -= self.v_down
        g.top_spike.y -= self.v_down
        
        # delete upper platforms/supplements/obstacles in order not to slow down the speed of execution
        for p in g.platforms:
            if p.y < -20:
                del p
        for s in g.supplements:
            if s.y < -20:
                del s
        for o in g.obstacles:
            if o.y < -20:
                del o
         
        
        self.v_down += self.delta_v_down # increase the downward speed 
        self.number = -1 # reset the platform type for the next loop

# put the game in the frame, and display the frame in the window

# we can use rectangles as platforms and produce animation mathematically
# sounds and images need to be added
# a csv file to instantiate objects needs to be created, with data readily available


my_gui = myGUI()
# instantiate the game somwhere

def keyPressed():
    if keyCode == LEFT:
        g.player.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        g.player.keyHandler[RIGHT] = True
    elif keyCode == UP:
        g.player.keyHandler[UP] = True
    elif keyCode == 80: # press 'p' to pause
        if g.pause:
            g.pause = False
            g.bgSound.play()
        else:
            g.pause = True
            g.bgSound.pause()
        g.pauseSound.rewind() # rewind the pause sound first before playing it
        g.pauseSound.play()
        
def keyReleased():
    if keyCode == LEFT:
        g.player.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        g.player.keyHandler[RIGHT] = False
    elif keyCode == UP:
        g.player.keyHandler[UP] = False
    
