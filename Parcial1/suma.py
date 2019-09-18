from sys import stdin

def back(t,i):
    if t==0:
        if r not in k:
            k.append(list(r))
            return 1
        else:
            return 0
    else:
        a=0
        for x in range(i,len(n),1):
            if 0<=t-n[x] and i<x:
                r.append(n[x])
                a+=back(t-n[x],x)
                r.pop()
        return a
def main():
    global n,r,k
    x=[int(i) for i in stdin.readline().split()]
    t=x[0]
    w=x[1]
    n=x[2:]
    while t!=0 and w!=0:
        print("Sums of "+str(t)+":")
        r=[]
        k=[]
        o=back(t,-1)
        if o>0:
            print(o)
        else:
            print("NONE")
        x=[int(i) for i in stdin.readline().split()]
        t=x[0]
        w=x[1]
        n=x[2:]

main()
