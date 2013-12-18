dict = {}
output1 = open("tempFile", "w")
for line in open('map'):
    temp = line.split("=")
    if(len(temp) > 1) :
        dict[temp[0]] = temp[1].strip("\n")
print dict


for line in open('inputFile') :
    line = line.strip(" ")
    i =0
    for letter in line :
        if(letter == "\n") :
            output1.write(dict.get("newline"))
        elif(letter == ",") :
            output1.write(dict.get("comma"))
        elif(letter == "!") :
            output1.write(dict.get("exc"))
        elif(letter == " ") :
            output1.write(dict.get("space"))
        elif(letter == ".") :
            output1.write(dict.get("dot"))
        else :
            output1.write(dict.get(letter))
output1.close()
input1 = open("tempFile", "r")
data = input1.readline()

cOutput = open("uber.c", "w")
ind = 0;
spaceData = dict.get("space")
spaceInd = 0
# put macros here 

cOutput.write("#define u printf(\"%c\",(" + "\n")
cOutput.write("#define I +32 )); " + "\n")
cOutput.write("#define E +1" + "\n")
cOutput.write("#define e +0" + "\n")
cOutput.write("#define R +2" + "\n")
cOutput.write("#define r +0" + "\n")
cOutput.write("#define T +4" + "\n")
cOutput.write("#define t +0" + "\n")
cOutput.write("#define A +8" + "\n")
cOutput.write("#define a +0" + "\n")
cOutput.write("#define X +16" + "\n")
cOutput.write("#define x +0" + "\n")
cOutput.write("#define B 65" + "\n")
cOutput.write("#define b 10" + "\n")
cOutput.write("#define i )); " + "\n")
cOutput.write("int main() {\n\n\n\n\n" )
for line in open('formatUber'):
    line = line.strip(" ")
    for letter in line:
        if(ind < len(data) and letter == "K") :
            cOutput.write(data[ind])
            ind=ind+1
        elif(ind >= len(data) and letter == "K") :
            ind=ind+1
            cOutput.write(spaceData[spaceInd])
            spaceInd=(spaceInd+1)%len(spaceData)
        else :
            cOutput.write(letter)
if spaceInd > 0:
    cOutput.write(spaceData[spaceInd : len(spaceData)])
cOutput.write("}\n" )
cOutput.close()