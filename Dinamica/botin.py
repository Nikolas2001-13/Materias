from sys import stdin
import sys
sys.setrecursionlimit(10000)

def back(w,i):
    if (w,i) in d:
        return d[(w,i)]
    else:
        if i<0 or w==0:
            res=0
        elif pesos[i]>w:
            res=back(w,i-1)
        elif pesos[i]<=w:
            res=max(back(w-pesos[i],i-1)+valor[i],back(w,i-1))
        d[(w,i)]=res
        return res

def main():
    global valor,pesos,d
    x=int(stdin.readline().strip())
    for i in range(x):
        d={}
        n,w=[int(s) for s in stdin.readline().strip().split()]
        valor=[int(s) for s in stdin.readline().strip().split()]
        pesos=[int(s) for s in stdin.readline().strip().split()]
        print(back(w,n-1))
        

main()
