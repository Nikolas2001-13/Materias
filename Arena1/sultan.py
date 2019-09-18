from sys import stdin

def queens(q,r):
    if r==8:
        rta=0
        for i in range(8):
            rta+=tablero[i][q[i]]
        num.append(rta)
    
    else:
        for j in range(8):
            legal=True
            for i in range(r):
                if (q[i]==j) or (q[i]==j+r-i) or (q[i]==j-r+i):
                    legal=False
            if legal:
                q[r]=j
                queens(q,r+1)

def main():
    global tablero,num
    x=int(stdin.readline())
    for i in range(x):
        tablero=[]
        num=[]
        for j in range(8):
            y=[int(a) for a in stdin.readline().strip().split()]
            tablero.append(y)
        queens([None]*8,0)
        d=[" "]*5
        yarit=(str(max(num)))
        for k in range(len(yarit)):
            d[5-len(yarit)+k]=yarit[k]
        print("".join(d))
        
main()
