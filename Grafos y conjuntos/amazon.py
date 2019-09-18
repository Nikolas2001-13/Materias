from sys import stdin

def dfs(vis,edge):
    cola=[0]
    while cola!=[]:
        u=cola.pop(0)
        if vis[u]==None:
            vis[u]=True
            for i in edge[u]:
                cola.append(i)
    return vis
         
def main():
    x=int(stdin.readline().strip())
    while x!=0:
        pares=[]
        lista=[int(i) for i in stdin.readline().strip().split()]
        for i in range(0,2*x,2):
            pares.append((lista[i],lista[i+1]))
        edge=[[] for i in range(x)]
        visitados=[None for i in range(x)]
        for i in range(len(pares)):
            org=[]
            for j in range(len(pares)):
                if i!=j:
                    distancia=(((pares[i][0]-pares[j][0])**2)+((pares[i][1]-pares[j][1])**2))**0.5
                    cord=(distancia,pares[j][0],pares[j][1],j)
                    org.append(cord)
            org.sort()
            for z in range(min(2,len(org))):
                edge[i].append(org[z][3])
        print(edge)
        mirar=dfs(visitados,edge)
        if None not in mirar:
            print("All stations are reachable.")
        else:
            print("There are stations that are unreachable.")  
        x=int(stdin.readline().strip())


main()
