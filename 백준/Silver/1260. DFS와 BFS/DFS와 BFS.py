import sys
from collections import deque

N, M, V = map(int,input().split())
visited_dfs = [[False] * (N+1) for _ in range((N+1))]
visited_bfs = [[False] * (N+1) for _ in range((N+1))]
route_dfs = [False] * (N+1)
route_bfs = [False] * (N+1)
c = 3

for i in range(M) :
    a,b = map(int, input().split())
    visited_bfs[a][b] = True
    visited_bfs[b][a] = True
    visited_dfs[a][b] = True
    visited_dfs[b][a] = True

def DFS(N, M, V) :
    print(V, end=" ")
    route_dfs[V] = True
    for i in range(N+1) :
        if visited_dfs[V][i] and not route_dfs[i] :
            visited_dfs[V][i] = False
            visited_dfs[i][V] = False
            DFS(N, M, i)

def BFS(N, M, V) :
    queue = deque()
    queue.append(V)
    print(V, end=" ")
    while queue :
        A = queue.popleft()
        V = A
        route_bfs[A] = True

        for i in range(N+1) :
            if visited_bfs[V][i] and not route_bfs[i] :
                print(i, end=" ")
                visited_bfs[V][i] = False
                visited_bfs[i][V] = False
                route_bfs[i] = True
                queue.append(i)

DFS(N,M,V)
print()
BFS(N,M,V)