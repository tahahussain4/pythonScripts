#Things that need to be changed come under PROPERTIES
from EDF_scheduling_algorithm import EDF
from Task_Description import Task
from graphics import *



def Display_EDF(interval,Task,Side_Len):
    Tasks = Task;
    #assinging EDF result to parmaters
    #[interval start,interval end ,task number]
    #PROPRTIES
    [EDF_sched,deadline_array] = EDF(interval,Tasks);

    start_interval_index = 0;
    end_interval_index = 1;
    Task_Index = 2;
    deadline_task_number = 0;
    deadline_time = 1
    Graph_Y_spacing = 4
    #rectangle algoritm for schedule
    #PROPERTIES
    x_perm_initial = 20
    y_perm_initial = 40;
    side_len = Side_Len;
    screen_width = 1280   #ex: 1280 for 720p                                                                                                        

    #initialize starting variables
    extend_line_counter = 1;
    x_initial = x_perm_initial;
    y_initial = (y_perm_initial) * Graph_Y_spacing  * extend_line_counter - side_len ;
    extend_line_counter = extend_line_counter + 1
    
    #displaying windows PROPERTIES (self adjusting)
    Graph_X = x_perm_initial*2+screen_width;
    Graph_Y = int (y_initial * int(((interval*side_len)/screen_width)+3) + side_len) 
    print(Graph_Y)
    print((interval*side_len)%screen_width)
    #windows
    #PROPERTIES
    win = GraphWin("EDF",Graph_X,Graph_Y);
    win.setBackground('white')

    #TITLE
    label = Text(Point(Graph_X/2, y_initial/2), 'EDF Schedule')
    label.draw(win);

    #forming repetitive squares with different colours and labelling them acorfingly
    colours = ["Salmon","Slate Blue","Medium Sea Green"];

    for i in range(0,interval):
        rect = Rectangle(Point(x_initial, y_initial), Point(x_initial+side_len,y_initial+side_len));
        rect.draw(win);
        #rect.setFill("green");
        rect.setFill(colours[i%(len(colours))]);

        #creating task numbers
        label = Text(Point(int(x_initial+side_len/2), int(y_initial+side_len/2)), str(EDF_sched[i][Task_Index]))
        label.setFill("white");
        label.setSize(int(side_len/4))
        label.draw(win);

        #creating sticking out lines
        dent_start = Point(int(x_initial),int(y_initial+side_len+side_len/3))
        dent_end = Point(int(x_initial),int(y_initial+side_len+side_len/3+side_len/4))
        dent = Line(dent_start,dent_end);
        dent.draw(win);
        
        #labelling scale
        label = Text(Point(x_initial, int(y_initial+side_len*2)), i)
        label.setFill("black");
        label.setSize(int(side_len/4))
        label.draw(win);
        
        same_deadlines=0;
        #drawing arrow for deadlines
        for y in deadline_array:
            if(y[deadline_time] == i):
                Draw_Arrow(win,x_initial,y_initial,side_len);
                
                #labelling last scal index                
                num_label = Text(Point(x_initial+(same_deadlines*side_len/4),int(y_initial+side_len*3.2)),y[deadline_task_number])
                num_label.setSize(int(side_len/5))
                num_label.draw(win);
                same_deadlines = same_deadlines+1;

            #boundary condition
            if(i == interval-1):
               if(y[deadline_time] == interval):
                    Draw_Arrow(win,int((x_initial+side_len)),y_initial,side_len);
                    num_label = Text(Point(x_initial+(same_deadlines*side_len/4)+side_len,int(y_initial+side_len*3.2)), y[deadline_task_number])
                    num_label.setSize(int(side_len/5))
                    num_label.draw(win);
                    same_deadlines = same_deadlines+1;
        
        x_initial = x_initial+side_len;

        #cchecking if scrren edge reached then move on to next line or printing last number when end
        #of interval
        if(x_initial+(side_len) > screen_width or  (i== interval-1) ):
            #printing end numbers
            label = Text(Point(x_initial, int(y_initial+side_len*2)), i+1)
            label.setFill("black");
            label.setSize(int(side_len/4))
            label.draw(win);

            #creating last sticking out line( the small lines for scale)
            dent_start = Point(int(x_initial),int(y_initial+side_len+side_len/3))
            dent_end = Point(int(x_initial),int(y_initial+side_len+side_len/3+side_len/4))
            dent = Line(dent_start,dent_end);
            dent.draw(win);
            
            x_initial = x_perm_initial
            y_initial = (y_perm_initial)* Graph_Y_spacing  * extend_line_counter  - side_len
            extend_line_counter = extend_line_counter + 1


            
        #RESETTING points if out of scrreen range
        
    #displaying legend
    
    win.getMouse();
    win.close();

#for printing out schedule instead of graphically displaying it
def Print_EDF(interval,frame_size,Task,print_deadlines):
    [tasks,deadlines]=EDF(interval,frame_size,Task);
    print("[INTERVAL , TASKS NUMBERS]");
    for  y in tasks:
        print (y);
    if(print_deadlines == True):
        print("\n");
        print("DEADLINES");
        print("[TASK NUMBER , DEADLINE TIME]");
        for y in deadlines:
            print (y);

def Draw_Arrow(win,x_initial,y_initial,side_len):
    arrow_one = Point(int(x_initial),int(y_initial+side_len*2.3))
    arrow_two = Point(int(x_initial-side_len/4),int(y_initial+side_len*2.3+side_len/4))
    arrow_three = Point(int(x_initial+side_len/4),int(y_initial+side_len*2.3+side_len/4))
    arrow_line = Point(int(x_initial),int(y_initial+side_len*2.3))
    arrow_line2 =Point(int(x_initial),int(y_initial+side_len*3))

    triangle = Polygon(arrow_one,arrow_two,arrow_three);
    triangle.setFill("black");
    triangle.draw(win);
    
    line = Line(arrow_line,arrow_line2);
    line.draw(win);
