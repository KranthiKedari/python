import cmath
n = input (" The number u want as starting bet ")

m = input (" The increment u want to use")


i =0
sum=0 
while i<25:
    sum = sum + (m**i) * n
    print "The total for ", i , " sequences is ", sum
    i=i+1
