from sys import stdin

def back(n,h,res,i):
    global s
    if i==n:
        print(res)
    else:
        for x in ["0","1"]:
            res+=str(x)
            if x=="1":
                if res.count("1")<=h:
                    back(n,h,res,i+1)
            else:
                if res.count("0")<=s:
                    back(n,h,res,i+1)
            res=res[:-1]                
def main():
    global s
    a=int(stdin.readline().strip())
    for k in range(a):
        stdin.readline()
        n,h=[int(s) for s in stdin.readline().strip().split()]
        res=""
        s=n-h
        back(n,h,res,0)
        print("")
main()
