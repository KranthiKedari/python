a=[100,130,200,300]
b=579
p=[0.13,0.15,0.30,0.34,0.34]
n = input (" The number of watts ur rig is using ")


tCost = 0

tUsage = n * 24 *30

pTier = 0
cUsage = 0
total = 0
cnt = 0
print "The total power usage per month is ", tUsage
print
print


while tUsage > 0 :
	units = 0
	usage =0
	if(cnt > 3):
		usage =tUsage
	else:
		usage = (a[cnt] - pTier) * b /100
		pTier =  a[cnt]	
	if tUsage <= usage:
		units = tUsage
	else :
		units = usage

	price =   units * p[cnt]
	total  = total + price
	print "the price for tier ", (cnt+1), " for ", units , " KWH at ", p[cnt] ," per KWH is ", price
	cnt = cnt + 1
	tUsage = tUsage - units



print "The power usage price per day is ", total/30
print "The total expected pge bill is going to be " , total 
