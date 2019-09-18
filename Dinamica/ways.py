from sys import stdin
import sys
sys.setrecursionlimit(99999999)

def din(x,i):
    if (x,i) in d:
        return d[(x,i)]
    else:
        if x==0:
            res=1
        elif i>=len(c) or x<0:
            res=0
        elif i<len(c) and x>=0:
            res=din(x-c[i],i)+din(x,i+1)
        d[(x,i)]=res
        return res
def main():
    global c,d
    c=[1,5,10,25,50]
    x=stdin.readline().strip()
    d={}
    while x!="":
        x=int(x)
        ans=din(x,0)
        if ans==1:
            print("There is only "+str(ans)+" way to produce "+str(x)+" cents change.")
        else:
            print("There are "+str(ans)+" ways to produce "+str(x)+" cents change.")
        x=stdin.readline().strip()

main()
    
