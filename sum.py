tempList = [-1,-3,5,4,-5]

result = {}
def findSum(sum, theList, left, right, list) :
    for number in theList[left:right]:
        #print sum , theList[left:right]
        if sum == number :
            print list
            list = []
        elif left != right:
            list.append(number)
            findSum(sum - number, theList, left + 1, right, list)

findSum(0, tempList, 0, len(tempList), [])