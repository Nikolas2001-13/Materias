from sys import stdin

class Conjunto:
    def __init__(self):
        self.p=self
        self.rank=0

def findS(x):
    if x!=x.p:
        x.p=findS(x.p)
    return x.p

def link(x,y):
    if x.rank>y.rank:
        y.p=x
    else:
        x.p=y
        if x.rank==y.rank:
            y.rank=y.rank+1
            
def union(x,y):
    link(findS(x),findS(y))       

def main():
    n,m=[int(i) for i in stdin.readline().strip().split()]
    q=1
    while n!=0 and m!=0:
        z=[Conjunto() for I in range(n)]
        for k in range(m):
            i,j=[int(s) for s in stdin.readline().strip().split()]
            union(z[i-1],z[j-1])
        a=0
        for J in z:
            if J==J.p:
                a+=1
        print("Case "+str(q)+":",a)
        q+=1
        n,m=[int(i) for i in stdin.readline().strip().split()]
        
main()
