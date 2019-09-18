from sys import stdin

def busquedaBinaria(n, item):

    primero = 0
    ultimo = len(n)-1
    
    while primero<=ultimo:
        mid = (primero + ultimo)//2
        if n[mid] == item:
            return "esta",mid
        else:
            if item < n[mid]:
                ultimo = mid-1
            else:
                primero = mid+1
    
    return "no esta",primero

def main():
    N=int(stdin.readline().strip())
    w=[int(i) for i in stdin.readline().strip().split()]
    Q=int(stdin.readline().strip())
    q=[int(i) for i in stdin.readline().strip().split()]
    n=list(set(w))
    n.sort()
    for i in q:
        con,ind=busquedaBinaria(n,i)
        if con=="esta":
            if ind!=0 and ind!=len(n)-1:
                print(n[ind-1],n[ind+1])
            elif ind==0:
                print("X",n[ind+1])
            elif ind==len(n)-1:
                print(n[ind-1],"X")
        else:
            if ind!=0 and ind!=len(n):
                print(n[ind-1],n[ind])
            elif ind==0:
                print("X",n[ind])
            elif ind==len(n):
                print(n[ind-1],"X")
                    

main()
