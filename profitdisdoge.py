n = input (" The number u using as starting bet ")

m = input (" The increment u are using use")


i =1
sum1=0
sum2=0 
print "Profit distribution"
h="Repetetion       "
j=2.0
while j<(m+0.2) :
    h= h + str(j) + "        "
    j = j+0.01
print h
j=2.0
while i<6: 
    s= str(i)+":      "
    while j<(m+0.5) :
        if(i==0) :
            sum2 = 0
        else :
            sum2 = sum2 + (j**(i-1)) * n
        sum1 = (m**i) * n
        s= s + str((sum1-sum2))+ "   "
        j=j+0.01
    print s
    i=i+1
