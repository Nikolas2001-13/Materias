from sys import stdin

def find(n):
    if parent[n]==n:
        return n
    return find(parent[n])

def union(u,v):
    ru=find(u)
    rv=find(v)
    if ru!=rv:
        if parent[ru]>parent[rv]:
            parent[rv]=ru
        else:
            parent[ru]=rv
            if rank[ru]==rank[rv]:
                rank[rv]+=1
        return True
    return False

def main():
    global parent,rank
    s=int(stdin.readline().strip())
    for i in range(s):
        stdin.readline().strip()
        n=int(stdin.readline().strip())
        coor=[]
        for j in range(n):
            x,y=[float(k) for k in stdin.readline().strip().split()]
            coor.append((x,y))
        parent={}
        rank={}
        comp={}
        for k in range(n):
            parent[k]=k
            rank[k]=1
            comp[coor[k]]=k
        dis=[]
        for k in range(n-1):
            for j in range(k+1,n):
                long=(((coor[k][0]-coor[j][0])**2)+((coor[k][1]-coor[j][1])**2))**0.5
                dis.append([long,coor[k],coor[j]])
        dis.sort()
        cont=0
        for k in dis:
            if union(comp[k[1]],comp[k[2]]):
                cont+=k[0]
        print('%.2f'%cont)
        if i!=s-1:
            print()
main()
