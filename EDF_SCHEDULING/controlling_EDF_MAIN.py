from Task_Description import *
from Displaying_EDF import *
from EDF_scheduling_algorithm import *

'''instructions
STEP 1:
-define the Tasks in an array
STEP 2:
-define side len of the square in pixels and the M4L2R8 interval period
-pass thorugh DisplaY_EDF() funciton with properties defined
'''

############################### STEP 1 ################################

#Task(number,period,release_time,execution_time,deadline)
Tasks = [];
Tasks.append(Task(1,6,1,1,2)) ;
Tasks.append(Task(2,5,0,2,3)) ;


################################ STEP 2 ###############################
#define interval that you want to display along witht he size of
#each scehduling frame 
interval = 100;

#state side_len for display purposes
side_len = 40

Display_EDF(interval,Tasks,side_len)


#if you dont want it displayed,call the functions below
#Print_EDF(interval,frame_size,Task,boolean print_deadlines):
#Print_EDF(interval,frame_size,Tasks,True);
