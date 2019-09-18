#Nikolás Bernal Giraldo-Code:2158547-Fecha:2/21/19

from sys import stdin

def merge(r):
    if len(r)==1:
        return r
    izq,der=divM(r)
    first=merge(izq)
    second=merge(der)
    return mergeSort(first,second)

def divM(r):
    mid=len(r)//2
    izq=r[:mid]
    der=r[mid:]
    return izq,der

def mergeSort(first,second):
    global p
    res=[]
    i,j=0,0
    while i<len(first) and j<len(second):
        if first[i]<second[j]:
            res.append(first[i])
            i+=1
        else:
            res.append(second[j])
            j+=1
            p+=len(first)-i
    res.extend(first[i:])
    res.extend(second[j:])
    return res

def main():
    global p
    n=int(stdin.readline())
    while n!=0:
        r=[]
        p=0
        for i in range(n):
            y=int(stdin.readline())
            r.append(y)
        merge(r)
        print(p)
        n=int(stdin.readline())
        r=[]

main()
