from sys import stdin

def back(acum,i,choices):
    if i==len(data):
        return
    elif acum==0:
        print(choices)
    else:
        for m in range(len(data)):
            choices[i]=data[m]
            if 
            
        
        

def main():
    global data
    n=[int(i) for i in stdin.readline().strip().split()]
    while n!="":
        c=n[0]
        data=n[2:]
        back(c,0,[0 for x in range(len(data))])
        
        n=[int(i) for i in stdin.readline().strip().split()]

main()
