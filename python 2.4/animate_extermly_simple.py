import pygame
import time
from graphics import *
listy = [1,1,1,1,1,1,1,1,1];

#intializing pos is po8+1
pos8 = 0;

direction  = 1;

#making sure direc
if(pos8 == 0):
     direction = 1;
elif(pos8 == len(listy) - 1):
     direction = -1;
else:
     direction = 1;



#for tetting
i=0

while(1):
    #reset list
    listy[2]= i
    for y in range(0,len(listy)):
        listy[y] = 1;
    #assign 8
    listy[pos8] = 8;

    #check if we are not at the end of an array
    if(pos8 == len(listy) - 1):
         direction = -1;
    elif(pos8 == 0):
         direction = 1;
    #increment array accordingly
    if(direction == -1):
        pos8-=1;
    elif(direction == 1):
        pos8+=1;
    print listy
    
    #not overloading the CPU
    time.sleep(1/60.0)
         
    
     
     
         
     
    

