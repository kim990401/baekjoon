import sys
sys.setrecursionlimit(10**9)

N, M = map(int,input().split())
graph = [[] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(N) :
    graph[i] = list(map(int,input().split()))

# N = 열, M = 행

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# dx, dy = x,y 좌표 방향

def dfs(x, y) :
    visited[y][x] = True
    for i in range(4) :
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < M and 0 <= new_y < N :
            if not visited[new_y][new_x] :
                if graph[new_y][new_x] > 0 :
                    dfs(new_x, new_y)
                elif graph[y][x] > 0 :
                    graph[y][x] -= 1

def year(N, M, ans) :
    global visited
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] and not visited[i][j] :
                cnt += 1
                if cnt >= 2 :
                    return print(ans)
                dfs(j,i)
    if cnt == 0 :
        return print(0)
    else :
        year(N, M, ans + 1)
    
year(N, M, 0)