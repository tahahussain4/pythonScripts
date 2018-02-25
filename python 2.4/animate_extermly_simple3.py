
import time
from graphics import *

def Circle_Create(circ):
    #creating circle
    Circ = Circle(Point(circ[1],circ[2]),circ[0]);
    Circ.draw(win);
    Circ.setFill("red");
    Circ.setOutline("purple");
    Circ.setWidth(5);
    return(Circ);
    
#making window
GraphX = 1000;
GraphY = 500;
win = GraphWin("simple animate",GraphX,GraphY);

#default background
background = "white"

#circle props
# MODIFY - radius and centre point r,x,y
circ = [25,50,GraphY/2];
circ2 = [25,50,GraphY/3];

#it is set to 1/60
frequency = 50.0

#in pixels/second
#this gives how much things should change for each frame
SpeedX = 1366/frequency;
SpeedY = 500/frequency;
acc = 9.81/frequency;
mass1 = 1;
mass2 = 2;
#coordinates of centre
nX = circ[1];
nY = circ[2];

Circ = Circle_Create(circ)
Circ2 = Circle_Create(circ2)



while(1):
    
    #calculate next points and ceate circle
    nX = int(nX + SpeedX/frequency)
    nY = int(nY + SpeedY/frequency)
    
    if(nX >= GraphX-circ[0] or nX<=0):
        SpeedX= SpeedX * -1;
        
    if(nY >= GraphY-circ[0] or nY<=0):
        SpeedY= SpeedY * -1;

    SpeedY = SpeedY - acc

    #energy to heat and stuff
    Circ.move(SpeedX,SpeedY);

    #resetting nX and nY
    nX = Circ.getCenter().getX();
    nY = Circ.getCenter().getY();
    
    #not overloading the CPU- making it run at 60 Hz
    time.sleep(1/frequency)


win.getMouse();
         
     


