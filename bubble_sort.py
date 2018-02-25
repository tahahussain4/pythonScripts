from graphics import *
import random
a =[]
#change the number to sort
#generates random number that need soting
number_to_sort = 50
for i in range(0,number_to_sort ):
    a.append(random.random() * 100)


#chagnable paraters
GraphX = 1000;
GraphY = 1000;
win = GraphWin("bubble sort",GraphX,GraphY);
bg = "white"
win.setBackground(bg);
colour = ["Medium Purple","Light Salmon","Lawn Green","Red"];
initial_index =0 ;
width = (GraphX-100)/len(a);
base = 500;

t = Text(Point(GraphX/2,GraphY/2),"Click To Begin");
t.setSize(35);
t.setOutline("blue");
t.draw(win)
win.getMouse();
t.setOutline(bg);

#setting up the rectangles for the fist time
for i in a:
    rec = Rectangle(Point(width*(initial_index+1),base-i*float(base-base/10)/max(a)),Point(width*(initial_index+2),base))
    rec.draw(win);
    rec.setFill(colour[initial_index%len(colour)])
    initial_index = initial_index+1;

#sorting alogrithm
iteration = 0;
t = Text(Point(GraphX-GraphX/20.0,GraphY/20.0),iteration);
t.setOutline("blue");
t.draw(win);


sort = False;
while(sort == False):
    
    sort = True;
    for i in range(0,len(a)-1):
        if(a[i]>a[i+1]):
            #erase rectangles
            rec = Rectangle(Point(width*(i+1),base-a[i]*float(base-base/10)/max(a)),Point(width*(i+2),base))
            rec.draw(win);
            rec.setFill("white");
            rec.setOutline("white");

            rec = Rectangle(Point(width*(i+2),base-a[i+1]*float(base-base/10)/max(a)),Point(width*(i+3),base))
            rec.draw(win);
            rec.setFill("white");
            rec.setOutline("white");

            #swapping algorithm
            temp = a[i];
            a[i] = a[i+1];
            a[i+1] = temp
            sort = False;
                    

            #redraw rectangles
            rec = Rectangle(Point(width*(i+1),base-a[i]*float(base-base/10)/max(a)),Point(width*(i+2),base))
            rec.draw(win);
            rec.setFill(colour[i%len(colour)]);

            rec = Rectangle(Point(width*(i+2),base-a[i+1]*float(base-base/10)/max(a)),Point(width*(i+3),base))
            rec.draw(win);
            rec.setFill(colour[(i+1)%len(colour)]);

            iteration = iteration +1;
            t.setText(iteration);
            
win.getMouse();
win.close();
