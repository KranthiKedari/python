ins = open("logFile", "r" )
ons = open( "logData", "w" )
ons1 = open( "logDetails", "w" )
arr= ["Level", "Category", "Sender", "Timestamp", "BODY",""]

for line in ins:
	if line.startswith("[Debug]") or line.startswith("[Info]") :
		str = line.split("]")
		i=0
		for word in str :
			if i>4 :
				i=5
			ons1.write(arr[i] +": "+ word.strip("[") + "\n")
			i=i+1
		ons1.write("\n\n")
		ons.write(line + "\n")
ins.close()
ons.close()
ons1.close()
