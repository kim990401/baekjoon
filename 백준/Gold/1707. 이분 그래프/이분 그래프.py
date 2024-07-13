import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(v,color) :
    global ans
    dfs_visited[v] = color
    for i in dfs_route[v] :
        if dfs_visited[i] == 0 :
            dfs(i,-color)
        elif dfs_visited[i] == dfs_visited[v] :
            ans = 'NO'
            return


T = int(input())

for i in range(T) :
    V, E = map(int, input().split())
    dfs_route = [[] for _ in range(V+1)]
    dfs_visited = [0] * (V+1)
    ans = 'YES'

    for i in range(E) :
        a, b = map(int,input().split())
        dfs_route[a].append(b)
        dfs_route[b].append(a)

    for i in range(V) :
        if dfs_visited[i] == 0 :
            dfs(i,1)
    print(ans)