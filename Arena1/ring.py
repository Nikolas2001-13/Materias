from sys import stdin
global p
p=[2,3,5,7,11,13,17,19,23]
def back(a,res,i):
    global p
    if len(res)==a:
        if res[0]+res[len(res)-1] in p:
            print(" ".join([str(k) for k in res]))
    else:
        for x in range(2,a+1):
            if x not in res:
                if res[-1]+x in p:
                    res.append(x)
                    back(a,res,i+1)
                    res.pop()

def main():
    a=(stdin.readline().strip())
    i=0
    res=[1]
    b=1
    while a!="":
        a=int(a)
        print("Case",str(b)+":")
        if a%2==0:
            back(a,res,i)
        b+=1
        print("")
        a = (stdin.readline().strip())


main()
