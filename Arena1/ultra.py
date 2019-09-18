from sys import stdin

def mergeSort(lista):
    if len(lista)==1:
        return lista

    izq,der=dividiralMedio(lista)
    lista1=mergeSort(izq)
    lista2=mergeSort(der)
    return merge(lista1,lista2)

def dividiralMedio(lista):
    middle=len(lista)//2
    return lista[0:middle],lista[middle:]

def merge(first,second):
    global p
    mergedList=[]
    i,j=0,0
    while i<len(first) and j<len(second):
        if first[i]<second[j]:
            mergedList.append(first[i])
            i+=1
        else:
            mergedList.append(second[j])
            j+=1
            p+=len(first)-i
    mergedList.extend(first[i:])
    mergedList.extend(second[j:])
    return mergedList


def main():
    global p
    n=int(stdin.readline().strip())
    r=[]
    while n!=0:
        p=0
        for i in range(n):
            a=int(stdin.readline().strip())
            r.append(a)
        mergeSort(r)
        print(p)
        n=int(stdin.readline().strip())
        r=[]

main()
