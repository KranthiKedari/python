n = input (" The number of the element in your list ")
i = 0
numbers = []
while i< n :
    numbers.append(input("Enter the number \n"))
    i=i+1

def insertSort(numList):
    count = len(numList)
    i = 1
    while i<count:
        j=i
        while(j > 0) :
            if(numList[j] < numList[j-1]) :
                numList[j], numList[j-1] = numList[j-1], numList[j]
                pass
            j= j-1
        i=i+1
    return numList


def bubbleSort(numList):
    return numList


numbers = insertSort(numbers)

i = 0
while i< len(numbers) :
    print numbers[i], "\n"
    i=i+1

