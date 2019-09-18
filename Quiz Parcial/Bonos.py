#Nikolas Bernal / Leonardo Galeano
from sys import stdin
def main():
    global p,d
    cases = int(stdin.readline().strip())
    for i in range(cases):
        d = {}
        p,t,a = (int(i) for i in stdin.readline().strip().split())
        p = [int(i) for i in stdin.readline().strip().split()]
        print(R(0,t,a))
def R(i,t,a):
    if (i,t,a) in d:
        return d[(i,t,a)]
    else:
        if i >= len(p):
            ans = 0
        elif t>0 and a>0:
            ans = min(R(i+3,t-1,a),R(i+5,t,a-1),p[i] + R(i+1,t,a))
        elif t == 0 and a != 0:
            ans = min(R(i+5,t,a-1),p[i] + R(i+1,t,a))
        elif a == 0 and t!= 0:
            ans = min(R(i+3,t-1,a),p[i] + R(i+1,t,a))
        elif a == 0 and t == 0:
            ans = p[i] + R(i+1,t,a)
        d[(i,t,a)] = ans
        return ans

main()
