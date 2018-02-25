'''
author : TAHA HUSSAIN,MacCAS
defining the properties of the task
not well tested
dont rely on this.
Structure :
-Realease tasks that need to be realased
-check if any deadlines are being met on tasks that are already running and reset if yes
-ready tasks that need to be readied
-coose closest deadline
-incremetn/decrement execution times
-
'''
from Task_Description import Task
#DESCRIPTION : takes in interval of the entire schedule,frame sizes and a list of
#type task
#RETURNS: EDF SCHED array and DEADLINES MISSED array
def EDF(interval,Task):
    EDF_schedule = []
    Tasks = Task;
    
    #deadline missed array
    deadline_array = []
    temp_array = []
    deadline_counter = 0;

    #checking if any released reached their period and were ready
    for current_time in range(0,interval):
        not_idle = False;
        
        for current_task in Tasks:
            if(current_task.release_time == current_time):
                current_task.released = True;
                
            if(current_task.released == True):
                #if actual counter = current value then raise deadline missed flag
                #task is stopped if dealine not met until its next period
                 if(current_task.actual_deadline == current_time):
                     if(current_task.run==True):
                        temp_array.append(current_task.number);
                        temp_array.append(current_time);
                        deadline_array.append(temp_array);
                        temp_array = []
                        current_task.run = False;
                        
                #boundary condition(predicting if dealine is missed in future
                #add to deadline missed array without stopping it
                 if(current_time==interval-1):
                    if(current_task.actual_deadline == current_time+1):
                        if(current_task.run==True):
                            temp_array.append(current_task.number);
                            temp_array.append(current_time+1);
                            deadline_array.append(temp_array);
                            temp_array = []

                    
                #redadying tasks
                 if(current_task.first_start == False):
                     if(float(current_time)%(current_task.release_time) == 0):
                         current_task.first_start = True;
                         current_task.run = True;
                         current_task.remaining_execution_time = current_task.execution_time;
                         current_task.actual_deadline = current_time + current_task.deadline;
                         current_task.times_readied = current_task.times_readied + 1;
                 else:
                     try:
                         if(float(current_time)%(current_task.period*current_task.times_readied + current_task.release_time) == 0):
                             current_task.run  = True;
                             current_task.remaining_execution_time = current_task.execution_time;
                             current_task.actual_deadline = current_time + current_task.deadline;
                             current_task.times_readied = current_task.times_readied + 1;
                     except ZeroDivisionError:
                             current_task.run  = True;
                             current_task.remaining_execution_time = current_task.execution_time;
                             current_task.actual_deadline = current_time + current_task.deadline;
                             current_task.times_readied = current_task.times_readied + 1;
                    
                    
        #seeing which task runs first according to EDF
        #smallest remaining execution time wins if equal EDF
        minimum_deadline = interval+100;  #some random big number
        for current_task in Tasks:
            if(current_task.run==True):
                not_idle = True;
                if(current_task.actual_deadline < minimum_deadline):
                    minimum_deadline = current_task.actual_deadline;
                    minimum_task = current_task;
                if(current_task.actual_deadline == minimum_deadline and current_time!=0):
                    if(current_task.number == EDF_schedule[current_time-1][2]):
                        minimum_task = current_task;
        
        #decrementing execution time.If time reaches 0 then turn run=false
        if(not_idle == True):
            minimum_task.remaining_execution_time = minimum_task.remaining_execution_time - 1;
            if(minimum_task.remaining_execution_time <=0):
                minimum_task.run=False;
            #print("("+str(current_time)+","+str(current_time+1)+")"+str(minimum_task.number));
            EDF_schedule.append([current_time,current_time+1,minimum_task.number]);
        else:
            #print("("+str(current_time)+","+str(current_time+1)+")"+" = IDLE");
            EDF_schedule.append([current_time,current_time+1,"IDLE"]);

    return(EDF_schedule,deadline_array);


    
             
