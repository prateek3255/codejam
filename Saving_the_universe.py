#https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
def check_def(s,p):
    cc=1
    for i in p:
        if i=='S':
            s=s-cc
        else:
            cc=cc*2  
    if s<0:
        return False
    else:
        return True
    
def swap(p,pos):
    p=list(p)
    p[pos],p[pos+1]=p[pos+1],p[pos]
    return ''.join(p)

t=int(input())
for test in range(t):
    s,p=input().split()
    s=int(s)
    swaps=0
    count=p.count('S')
    ip=False
    while not(check_def(s,p)):
        if p.find('C')!=-1 and p.find('C')!=count:
            p=swap(p,p.find('C'))
            swaps+=1
        else:
            ip=True
            break
    if not(ip):
        print("Case #{}: {}".format(test+1, swaps))
    else:
        print("Case #{}: {}".format(test+1, 'IMPOSSIBLE'))
            
    

