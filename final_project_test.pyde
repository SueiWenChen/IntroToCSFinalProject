import os
path = os.getcwd() + '/'
inputFile = open(path+'data.csv','r')

class Platform:
    def __init__(self,x,y): # (x,y): upper-left corner, w = width
        self.x = x
        self.y = y
        self.w = 160
        # self.img = loadImage(path+'images/'+img)
    
    # def update(self):
    #     self.y -= g.v
    
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
        fill(192,192,192)
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
        # if p.flip_range == []:
        #     fill(0)
        # else:
        #     fill(255-255*(p.y-p.flip_range[1])/20)
        fill(0)
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


class Top_spike:
    def __init__(self):
        self.y = 0
    def display(self):
        noStroke()
        fill(192,192,192)
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
        triangle(640,self.y,800,self.y-80,800,self.y)
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


class Game:
    def __init__(self):
        self.y = 0 # the "apparent" ceiling height of the game
        self.v_down = 10 # velocity of the downward movement
        # self.bgd = bgd
        self.score = self.y//800
        # instantiate objects
        # self.player = Player(380,400)
        self.platformList = []
        self.s = Top_spike()
        self.b = Bottom_spike()
        self.real = Tube(560)
        self.fake = Tube(240)
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
                self.platformList.append(Conveyor(int(line[1]),int(line[2]),int(line[3])))
            elif int(line[0]) == 5:
                self.platformList.append(Spring(int(line[1]),int(line[2])))
            
    
    def display(self):
        for p in self.platformList:
            p.display()
        self.s.display()
        self.b.display()
        self.real.display()
        self.fake.display()
        # self.player.display()
            
    
    def update(self):
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
        
        # # delete upper platforms/supplements/obstacles in order not to slow down the speed of execution
        # for p in g.platforms:
        #     if p.y < -20:
        #         del p
        # for s in g.supplements:
        #     if s.y < -20:
        #         del s
        # for o in g.obstacles:
        #     if o.y < -20:
        #         del o
        # level = self.p.y//800
        # self.v_down = [1,1.3,1.6,1.9,2,2.2,2.5,2.8,3.1,3.4]  
        if self.b.y < 801:
            self.v_down = 0      

        # self.number = -1 # reset the platform type for the next loop
                                                
g = Game()                
        
def setup():
    size(1200,800)
    background(255)
    fill(0)
    rect(800,0,5,800)
    
def draw():
    background(255)
    fill(0)
    rect(800,0,5,800)
    g.display()
    g.update()
