Stop = False
i=0
try:
    while Stop == False:
        if(pow(2,i)%7.0 == 0):
            print(i)
            Stop == True
            break
        i=i+1
except OverflowError:
    print (i) 
    
