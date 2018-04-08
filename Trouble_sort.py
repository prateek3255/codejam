#https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
def TroubleSort(l1):
    done=False
    while not done:
        done=True
        for i in range(len(l1)-2):
            if l1[i]>l1[i+2]:
                done=False
                l1[i],l1[i+2]=l1[i+2],l1[i]
    return l1


t=int(input())
for test in range(t):
    _=int(input())
    l=list(map(int,input().split()))
    tl=list(l)
    tl=TroubleSort(tl)
    l.sort()
    ind=0
    if not tl==l:    
        for i in range(len(l)):
            if l[i]!=tl[i]:
                ind=i
                break
        print("Case #{}: {}".format(test+1, ind))
    else:
        print("Case #{}: {}".format(test+1, 'OK'))
                
    

