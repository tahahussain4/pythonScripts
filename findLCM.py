#least common multiple
#parameter should be an array
#I increment by the maximum value as it has to be divisble either ways
def findLCM(x):
    print(x);
    #variable to be divided by
    maximum=max(x)
    LCM = maximum;
    Run = True;

    #setting a not divisible flag
    NotDiv = False;

    ##if one variable is not perfectly divisible then set a flag##
    while(Run == True):
        #check if divisble (set flag if not)
        for i in range(0,len(x)):
            if(LCM%x[i] != 0):
                NotDiv = True;
                break;
        #end while loop if flag not set
        if(NotDiv == False):
            print("LCM =",LCM);
            Run = False;

        #reset flag and increment by an appropriate value
        NotDiv = False;
        LCM= LCM + maximum;
    print("Done")
    
#testing
var=[3,5,8]
findLCM(var)

