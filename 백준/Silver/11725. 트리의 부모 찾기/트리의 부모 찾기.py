import sys
sys.setrecursionlimit(10**9)

N = int(input())
dfs_route = [[] for _ in range(N+1)]
dfs_visited = [False] * (N+1)

for i in range(1,N) :
    a, b = map(int,input().split())
    dfs_route[a].append(b)
    dfs_route[b].append(a)

def dfs(v) :
    for i in dfs_route[v] :
        if not dfs_visited[i] :
            dfs_visited[i] = v
            dfs(i)
dfs(1)
for i in range(2,N+1) :
    print(dfs_visited[i])