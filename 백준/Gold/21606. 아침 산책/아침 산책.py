import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
A = input()
cnt = 0
dfs_route = [[] for _ in range(N+1)]
dfs_visited = [0] * (N+1)
dfs_position = [1] * (N+1)
dfs_value = [1] * (N+1)

for i in range(1,len(A)+1) :
    if A[i-1] == '0' :
        dfs_position[i] = 0
        dfs_value[i] = 0

for i in range(N-1) :
    a, b = map(int,input().split())
    dfs_route[a].append(b)
    dfs_route[b].append(a)

def dfs(v) :
    global cnt
    dfs_visited[v] = 1
    if not dfs_position[v] :
        for i in dfs_route[v] :
            if not dfs_visited[i] :
                dfs(i)
                dfs_value[v] += dfs_value[i]
    else :
        for i in dfs_route[v] :
            if not dfs_visited[i] :
                dfs(i)
                cnt += (dfs_value[i]+1) * dfs_value[i] // 2

for i in range(1,N+1) :
    if dfs_position[i] == 1 :
        dfs(i)
        break

print(cnt*2)