a=1
b=1

n = 15
index = 1
fnPrev = 1
fnPrevPrev = 1;
fnCurr =0
print fnPrevPrev
print fnPrev
while index<n:
    fnCurr = fnPrev + fnPrevPrev
    print fnCurr
    fnPrevPrev = fnPrev
    fnPrev = fnCurr
    index=index+1