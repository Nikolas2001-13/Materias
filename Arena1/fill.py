from sys import stdin

def bus(m):
    prim=max(c)
    ult=sum(c)

    while prim<ult:
        mid=(prim+ult)//2
        a=0
        res=1
        for i in c:
            if a+i<=mid:
                a+=i
            else:
                a=i
                res+=1
        if res<=m:
            ult=mid
        else:
            prim=mid+1
    return ult

    
def main():
    global c
    x=stdin.readline().strip()
    while x!="":
        n,m=[int(i) for i in x.split()]
        c=[int(i) for i in stdin.readline().strip().split()]
        print(bus(m))
        x=stdin.readline().strip()

main()
    
