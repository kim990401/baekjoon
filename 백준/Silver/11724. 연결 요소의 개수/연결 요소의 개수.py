import sys
input = sys.stdin.readline
N, M = map(int,input().split())

dfs_visited = [[False]*(N+1) for _ in range(N+1)]
dfs_route = [False] * (N+1)
for i in range(M) :
    a, b = map(int,input().split())
    dfs_visited[a][b] = True
    dfs_visited[b][a] = True
ans = 0

def dfs(v) :
    dfs_route[v] = True
    for i in range(1,N+1) :
        if dfs_visited[v][i] and not dfs_route[i] :
            dfs(i)

for i in range(1,N+1) :
    if dfs_route[i] == True :
        continue 
    dfs(i)
    ans += 1

print(ans)