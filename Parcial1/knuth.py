from sys import stdin

def back(r,i):
    if len(r)==len(x):
        w=[str(q) for q in r]
        print("".join(w))
    else:
        for k in range(len(r)+1):
            res=r[:k]+list(x[i])+r[k:]
            back(res,i+1)
            
def main():
    global x
    x=stdin.readline().strip()
    while x!="":
        r=[x[0]]
        back(r,1)
        print()
        x=stdin.readline().strip()     

main() 
