import cmath
n = input (" The total number of doges u got ")

m = input (" The total number of sequences u want")


i =2.0
while i<3.0:
    value = n/((i**(m+1) - 1)/(i-1))
    print "The initial bet for factor ", i, " is ", value
    i=i+0.01
