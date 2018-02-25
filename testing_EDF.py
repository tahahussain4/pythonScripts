#must import shit
#
from EDF_scheduling_algorithm import EDF
from Task_Description import Task
from graphics import *

#creating array of tasks
#props that need to be changed
Tasks = []
Tasks.append(Task(1,10,5,2,10)) 
interval = 30  
frame_size = 1;

#assinging EDF result to parmaters
#[interval start,interval end ,task number]
[EDF_sched,deadline_array] = EDF(interval,frame_size,Tasks);
start_interval_index = 0;
end_interval_index = 1;
Task_Index = 2;

#rectangle algoritm for shcedule PROPERTIES
x_initial = 20;
y_initial = 40;
side_len = 40;


#displaying windows PROPERTIES (self adjusting)
Graph_X = x_initial*2+side_len*interval;
Graph_Y = (y_initial+side_len) * 2

#windows PROPERTIES
win = GraphWin("EDF",Graph_X,Graph_Y);
win.setBackground('white')

#TITLE
label = Text(Point(Graph_X/2, 20), 'EDF Schedule')
label.draw(win);

#forming repetitive squares with different colours and labelling them acorfingly
colours = ["red","blue","green"];
for i in range(0,interval):
    rect = Rectangle(Point(x_initial, y_initial), Point(x_initial+side_len,y_initial+side_len));
    rect.draw(win);
    #rect.setFill("green");
    rect.setFill(colours[i%(len(colours))]);

    label = Text(Point(x_initial+side_len/2, y_initial+side_len/2), str(EDF_sched[i][Task_Index ]))
    label.setFill("white");
    label.draw(win);
    
    x_initial = x_initial+side_len;

#to pause
win.getMouse();
win.close();
#this is for you click on the application    
#if __name__ == "__main__":
#    test()
