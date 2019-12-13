# this is a modified version of the game "NS-SHAFT"
import os
path = os.getcwd() + '/'
inputFile = open(path+'data.csv','r')

class Platform:
    def __init__(self,x,y): # (x,y): upper-left corner, w = width
        self.x = x
        self.y = y
        self.w = 160
        # self.img = loadImage(path+'images/'+img)
    
    def display(self):
        # image(img,#x,#y,#width,#height)
        noStroke()
        fill(25,100,122)
        rect(self.x,self.y,160,20)
            
class Ord(Platform):
    def __init__(self,x,y): # num is for indentification of platform types
        Platform.__init__(self,x,y)
        self.num = 0

class Fake(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.num = 1

class Spiky(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.num = 2
    def display(self):
        noStroke()
        fill(200,200,200)
        rect(self.x,self.y,160,5)
        i = 0
        while i < 16:
            triangle(self.x+10*i,self.y,self.x+10*i+5,self.y-15,self.x+10*(i+1),self.y)  
            i += 1      
    
class Flip(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.num = 3
    def display(self):
        # the platform gradually 'disappers'
        noStroke()
        if g.player.flip_range == []:
            fill(0)
        else:
            fill(0,0,0,255-255*(g.player.y-g.player.flip_range[1]))
        rect(self.x,self.y,160,20)

class Conveyor(Platform):
    def __init__(self,x,y,v):
        Platform.__init__(self,x,y)
        self.num = 4
        self.v = v # +5: right; -5: left
    def display(self):
        noStroke()
        fill(0,0,255)
        rect(self.x,self.y,160,20)
        fill(255,255,0)
        if self.v > 0:
            triangle(self.x+60,self.y+5,self.x+60,self.y+15,self.x+100,self.y+10)
        else:
            triangle(self.x+100,self.y+5,self.x+100,self.y+15,self.x+60,self.y+10)
    
    
class Spring(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)
        self.num = 5
    def display(self):
        noStroke()
        fill(0,0,255)
        rect(self.x,self.y,160,20)
        fill(255,255,0)
        triangle(self.x+80,self.y+5,self.x+60,self.y+15,self.x+100,self.y+15)        

# class Obstacles:
#     def __init__(self,x,y,img): # (x,y): upper-left corner
#         self.x = x
#         self.y = y
#         self.w = w # width
#         self.h = h # height
#         self.img = loadImage(path+'images/'+img)

# class Supplements:
#     def __init__(self,x,y,l,w,img): # (x,y): upper-left corner
#         self.x = x
#         self.y = y
#         self.h = h # height
#         self.w = w # width
#         self.img = loadImage(path+'images/'+img)
 
class Top_spike:
    def __init__(self):
        self.y = 0
    def display(self):
        noStroke()
        fill(200,200,200)
        i = 0
        while i < 80:
            triangle(10*i,0,10*i+5,10,10*(i+1),0)  
            i += 1  

class Bottom_spike:
    def __init__(self):
        self.y = 7200
    def display(self):
        noStroke()

        fill(169,169,169)
        i = 0 
        while i < 10:
            triangle(80*i-40,self.y,80*i,self.y-80,80*(i+1)-40,self.y)  
            i += 1
        triangle(760,self.y,800,self.y-80,800,self.y)
        fill(192,192,192)
        i = 0
        while i < 10:
            triangle(80*i,self.y,80*i+40,self.y-80,80*(i+1),self.y)  
            i += 1 

class Tube:
    def __init__(self,x):
        self.x = x
        self.y = 7080
    def display(self):
        strokeWeight(2)
        stroke(0)
        fill(173,255,47)
        rect(self.x-60,self.y,120,120)
        ellipse(self.x,self.y,120,40)
        fill(0)
        ellipse(self.x,self.y,110,30)
    
            
class HealthBar:
    def __init__(self):
        self.h = 12
    
    def display(self): # h <= 12
        textSize(60)
        fill(210,210,0)
        text("LIFE",840,200)
        strokeWeight(5)
        stroke(0)
        noFill()
        rect(980,160,185,40)
        fill(255,255,0)
        noStroke()
        for i in range(self.h):
            rect(983+15*i,163,15,35)


class Player:
    def __init__(self,x,y): # (x,y): center, h: health
        self.x = x
        self.y = y
        self.r = 35
        self.vx = 0
        self.v_fall = 0
        # self.dvx = 0 # velocity caused by conveyor belts
        self.fv = 0.05 # velocity of flipping down
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
        self.h = 12
        self.number = 0 # the type of platform on which the player stands
        self.landed = 0 # 1 means landed and updates are yet to be made; 0 otherwise
        self.flip_range = [] # the range within which the player flips
        self.on_a_platform = True
        self.on_flip = False
        self.btm = 0 # the bottom of each flip

    def update(self): # if the player is on a proper platform, stop falling; otherwise fall
        # self.on_a_platform = False
        # for p in g.platformList:  # check every platform in the platform list
        #     if p.num != 1: # not a deceptive one
        #         if self.y + self.r == p.y and p.x <= self.x + 10 and self.x-10 <= p.x+p.w: #if on a platform
        #             self.y = p.y - self.r - g.v_down
        #             self.v_fall = 0
        #             self.on_a_platform = True
        #             self.number = p.num # keep track of the type of platform the player is on
        #             if p.num == 4: # if on a belt, keep track of the velocity
        #                 self.dvx = p.v
        #             break
        #         elif self.y+self.r<p.y and self.y+self.r+self.v_fall>=p.y-g.v_down and p.x<=self.x<=p.x+p.w:  # if during an update the player hits a platform
        #             self.v_fall = p.y - (self.y+self.r) - g.v_down # land on a platform
        #             self.landed = 1
        #             self.on_a_platform = True
        #         #     if p.num == 3:
        #         #         self.flip_range = [p.y,p.y+20]
        #             break
        #     if p.num == 1 and self.y+self.r<p.y and self.y+self.r+self.v_fall>=p.y-g.v_down and p.x<=self.x<=p.x+p.w: 
        #         g.platformList.remove(p) # del the fake platform once the player reaches it
        #         # sound effect of disappearing
        # # if self.flip_range != [] and self.y + self.r/2 >= self.flip_range[0]:
        # #     self.v_fall = 0.05
        # #     self.flip_range[0] -= g.v_down
        # #     self.flip_range[1] -= g.v_down
        # #     if self.y-self.r/2 > self.flip_range[1]:
        # #         self.flip_range = []
        # #         self.number = -1
        # #         self.on_a_platform = False
        # if not self.on_a_platform and self.flip_range == []:
        #     self.v_fall += 0.4
        #     self.flip_range = []
        
    # if not self.die():        
        self.on_a_platform = False
        for p in g.platformList:  # check every platform in the platform list
            if self.y + self.r == p.y and p.x <= self.x + 10 and self.x-10 <= p.x+p.w: #if on a platform
                self.on_a_platform = True
                if p.num == 1: # if on a fake one
                    g.platformList.remove(p)
                    # sound effect of disappearing
                    self.landed = 0
                else:
                    self.on_a_platform = True
                if p.num == 3:
                    self.v_fall = 0.5-g.v_down
                    self.on_flip = True
                    self.btm = p.y + 20
                elif p.num == 5:
                    self.v_fall = -15
                else:
                    self.v_fall = - g.v_down
                    if p.num != 2 and self.h < 12 and self.landed == 1:
                        self.h += 1
                        self.landed = 0
                    if p.num == 2 and self.landed == 1:
                        self.h -= 5
                        self.landed = 0
                    if p.num == 4:
                        self.vx += p.v      
                break
            if self.y+self.r<p.y and self.y+self.r+self.v_fall>=p.y-g.v_down and p.x<=self.x<=p.x+p.w:  # if during an update the player hits a platform
                self.v_fall = p.y - (self.y+self.r) - g.v_down # land on a platform
                self.landed = 1
                self.on_a_platform = True
                break
        if self.on_flip:
            if self.y -self.r < self.btm:
                self.v_fall = 0.5-g.v_down
            else:
                self.btm = 0
                self.on_flip = False
        elif not self.on_a_platform:
            self.v_fall += 0.4
                    
        if self.keyHandler[LEFT]:
            self.vx = -6
        elif self.keyHandler[RIGHT]:
            self.vx = 6
        else:
            self.vx = 0
    
        if self.keyHandler[UP] and self.on_a_platform==True:
            # self.jumpSound.rewind()
            # self.jumpSound.play()
            self.v_fall = -10

        # move
        self.x += self.vx
        self.y += self.v_fall       
        # the player is not allowed to go outside the view
        if self.x - self.r < 0:
            self.x = self.r 
        if self.x + self.r > 800:
            self.x = 800 - self.r
        # # # the player is cannot run into obstacles or platforms
        # for o in g.obstacles:
        #     if self.keyHandler[LEFT] and o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h:
        #         self.x = o.x+o.w
        #     if self.keyHandler[RIGHT] and o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h:
        #         self.x = o.x
        #     if o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h and self.v_fall>0:
                


    
    # def new_health(self):   
        # for s in g.supplements: # replenishment
        #     if s.x <= self.x <= s.x + s.w and s.y <= self.y <= s.y + s.h:
        #         self.h = 12
        #         del s
        #         break

    def die(self):
        if self.h <= 0 or self.y <= self.r:
            return True

    # def update(self):
    #     if not self.die():
    #         # self.new_health()
    #         g.h.h = self.h        
            
    #         if self.keyHandler[LEFT]:
    #             self.vx = -6
    #         elif self.keyHandler[RIGHT]:
    #             self.vx = 6
    #         else:
    #             self.vx = 0

    #         self.gravity()
    #         # self.effects() # update according to the type of platform                
    #         if self.keyHandler[UP] and self.on_a_platform==True:
    #             # self.jumpSound.rewind()
    #             # self.jumpSound.play()
    #             self.v_fall = -10
    
    #         # move
    #         self.x += self.vx
    #         self.y += self.v_fall       
    #         # the player is not allowed to go outside the view
    #         if self.x - self.r < 0:
    #             self.x = self.r 
    #         if self.x + self.r > 800:
    #             self.x = 800 - self.r
    #         # # # the player is cannot run into obstacles or platforms
    #         # for o in g.obstacles:
    #         #     if self.keyHandler[LEFT] and o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h:
    #         #         self.x = o.x+o.w
    #         #     if self.keyHandler[RIGHT] and o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h:
    #         #         self.x = o.x
    #         #     if o.x<self.x<o.x+o.w and o.y<self.y<o.y+o.h and self.v_fall>0:
                    

    #         self.landed = 0 # updates are done
        
        # if self.die():
            # sound effect
            # display a pop-up window showing 'game over' and 'press [something] to restart'
            # restart the game
            
    
    def display(self):
        fill(0)
        circle(self.x,self.y,70)    

# class Background:
#     def __init__(self,img):
#         self.img = loadImage(path+'images/'+img)

class Game:
    def __init__(self):
        self.y = 0 # the "apparent" ceiling height of the game
        self.v_down = 1 # velocity of the downward movement
        # self.bgd = bgd
        self.level = 9
        self.t = 0
        # instantiate objects
        self.player = Player(480,100)
        self.s = Top_spike()
        self.b = Bottom_spike()
        self.real = Tube(560)
        self.fake = Tube(240)
        self.h = HealthBar()
        self.platformList = []        
        for line in inputFile:
            line = line.strip().split(",")
            if int(line[0]) == 0:
                self.platformList.append(Ord(int(line[1]),int(line[2])))
            elif int(line[0]) == 1:
                self.platformList.append(Fake(int(line[1]),int(line[2])))
            elif int(line[0]) == 2:
                self.platformList.append(Spiky(int(line[1]),int(line[2])))
            elif int(line[0]) == 3:
                self.platformList.append(Flip(int(line[1]),int(line[2])))
            elif int(line[0]) == 4:
                self.platformList.append(Conveyor(int(line[1]),int(line[2]),float(line[3])))
            elif int(line[0]) == 5:
                self.platformList.append(Spring(int(line[1]),int(line[2])))
            
    def display(self):
        fill(0)
        rect(800,0,5,800)
        noStroke()
        fill(0,250,150,50)
        rect(0,0,800,800)
        fill(0)
        rect(800,0,5,800)
        fill(0,200,100,200)
        rect(805,0,400,800)
        textSize(80)
        fill(255*(0.3*sin(self.t)+0.3),0,0)
        text('ROLL!!!!!',840,100)
        fill(255*(0.2*sin(self.t)+0.5),0,0)
        textSize(300)
        text(str(self.level)+'F',820,500)
        textSize(80)
        stroke(0)
        fill(0,255,0)
        rect(865,625,280,90)
        fill(150,0,0)
        text("START",880,700)
        self.h.display()
        for p in self.platformList:
            p.display()
        self.s.display()
        self.b.display()
        self.real.display()
        self.fake.display()
        self.player.display()

            
    
    def update(self):
        self.player.update()
        # move up all the objects (potentially except the player) and the scope appears to move down 
        for p in self.platformList:
            p.y -= self.v_down
        self.b.y -= self.v_down
        self.real.y -= self.v_down
        self.fake.y -= self.v_down
        # for o in self.obstacles:
        #     o.y -= self.v_down
        # for s in self.supplements:
        #     s.y -= self.v_down
        
        # delete upper platforms/supplements/obstacles in order not to slow down the speed of execution
        for p in self.platformList:
            if p.y < -20:
                self.platformList.remove(p)
        # for s in self.supplements:
        #     if s.y < -20:
                # self.platformList.remove(s)
        # for o in self.obstacles:
        #     if o.y < -20:
                # self.platformList.remove(o)
        self.level = int((self.b.y+801)//800)  
        self.v_down = [0,4.5,4,3.5,3,2.5,2,1.5,0.8,0.8][self.level - 1]
        if self.b.y < 800:
            self.v_down = 0
            self.level = 1
    

        self.player.number = -1 # reset the platform type for the next loop
        self.t += 0.05 # change of text color
                                 
# sounds


g = Game()                
        
def setup():
    size(1200,800)
    background(255)
    fill(0)
    rect(800,0,5,800)
    
def draw():
    background(255)
    g.display()
    g.update()
    print(g.player.y)
    print(g.player.on_a_platform)

    






# def mousePressed(): # it executes the indented code after it whenever the mouse is pressed
#     g.mouseHandler['Clicking'] = True
# def mouseReleased(): # it executes the indented code after it whenever the mouse is released
#     g.mouseHandler['Clicking'] = False
# def mouseClicked(): # it executes the indented code after it whenever the mouse is clicked
#     global restart
#     if g.mouseHandler['Clicking'] == True:
#         restart = True   
        
# use "noLoop" to stop the loop?
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
