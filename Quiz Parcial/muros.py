from sys import stdin

def din(n):
    if n in d:
        return d[n]
    else:
        if n==1:
            res=1
        elif n==2:
            res=2
        else:
            res=din(n-1)+din(n-2)
        d[n]=res
        return res

def main():
    global d
    n=int(stdin.readline().strip())
    d={}
    while n!=0:
        print(din(n))
        n=int(stdin.readline().strip())

main()
