from sys import stdin

def bfs(g,v):
    cola=[0]
    v[0]=1

    while cola:
        node=cola.pop(0)
        for x in range(0,len(v)):
            if not g[node][x]:
                continue
            if v[x]==0:
                v[x]=1 if v[node]==0 else 0
                cola.append(x)
            elif v[node]==v[x]:
                return False
    return True

def main():
    n=int(stdin.readline().strip())
    while n!=0:
        arc=int(stdin.readline().strip())
        grafo=[]
        for s in range(n):
            grafo.append([0]*n)
        for s in range(arc):
            i,j=[int(k) for k in stdin.readline().strip().split()]
            grafo[i][j]=1
            grafo[j][i]=1
        visited=[0]*n
        color=bfs(grafo,visited)
        if color:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
        n=int(stdin.readline().strip())

main()
