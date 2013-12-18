def findSolution(open, close, str, balance) :
    if(open == 0 and close == 0):
        print str

    if(open > 0) :
        findSolution(open-1,close, str + "{", balance + 1)
    if(close>0 and balance > 0) :
        findSolution(open, close-1 , str + "}", balance -1)

findSolution(3, 3, "", 0)

