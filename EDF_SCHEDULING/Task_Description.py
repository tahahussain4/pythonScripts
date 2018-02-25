'''
Holding all the properties of a task
'''
class Task:
    ready = False;
    run = False;
    released = False;
    #first start is for implemeting realease time functionality
    first_start = False;
    number = 0;
    period = 0;
    execution_time = 0;
    remaining_execution_time = 0;
    deadline = 0;
    actual_deadline = 0;
    release_time = 0;
    times_readied = 0;
 
    def __init__(self,number,period,release_time,execution_time,deadline):
        self.number = number;
        self.period = period;
        self.release_time = release_time;
        self.execution_time = execution_time;
        self.remaining_execution_time =execution_time;
        self.deadline  = deadline;
        #first actual deadline
        self.actual_deadline = deadline+release_time;
        if(release_time==0):
            self.first_start = True;
