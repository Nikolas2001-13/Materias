from sys import stdin

def back(x,z):
    if (x,z) in d:
        return d[(x,z)]
    else:
        if x==0 and z==0:
            res=0
        elif x==0 and z!=0:
            res=z
        elif x!=0 and z==0:
            res=x
        elif y[x-1]==w[z-1]:
            res=back(x-1,z-1)
        elif y[x-1]!=w[z-1]:
            res=min(back(x,z-1)+1,back(x-1,z)+1,back(x-1,z-1)+1)
        d[(x,z)]=res
        return res
        

def main():
    global y,w,d
    a=stdin.readline().strip().split()
    while a!=[]:
        d={}
        b=stdin.readline().strip().split()
        x=int(a[0])
        z=int(b[0])
        y=a[-1]
        w=b[-1]
        print(back(x,z))
        a=stdin.readline().strip().split()
        
main()
