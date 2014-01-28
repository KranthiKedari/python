import cmath
n = input (" The number u using as starting bet ")

m = input (" The increment u are using use")


i =0
sum1=0
sum2=0 
while i<25:
    if(i==0) :
        sum2 = 0
    else :
        sum2 = sum2 + (m**(i-1)) * n
    sum1 = (m**i) * n
    print "The profit for ", i ," failures is ", sum1 , " - ", sum2 , "   =   ",(sum1-sum2)
    i=i+1
