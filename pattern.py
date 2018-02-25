#patterm 2,6,12,20.....
n=2  #start at two
prevVal=2

for i in range(0,77):
    prevVal = prevVal + 2*n
    print str(n)+"    "+str(prevVal)
    n=n+1
