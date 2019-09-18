#Nikolás Bernal Giraldo-Code:2158547-Fecha:2/21/19

from sys import stdin

def bus(n,i):
    first=0
    ult=len(n)-1
    while first<=ult:
        mid=(first+ult)//2
        if n[mid]==i:
            return True,mid
        else:
            if i<n[mid]:
                ult=mid-1
            else:
                first=mid+1
    return False,first

def main():
    x=int(stdin.readline())
    n=[int(i) for i in stdin.readline().strip().split()]
    y=int(stdin.readline())
    q=[int(i) for i in stdin.readline().strip().split()]
    n=list(set(n))
    n.sort()
    for i in q:
        mir,ind=bus(n,i)
        if mir:
            if ind==0:
                print("X")
            else:
                print(n[ind-1])
        else:
            if ind-1<0:
                print("X")
            else:
                print(n[ind-1])
        

main()
