N = int(input())
map = [[] for _ in range(N)]
visited = [[False]*N for _ in range(N)]
for i in range(N) :
    map[i] = list(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
arr = []

def dfs(x, y) :
    global cnt
    cnt += 1
    for i in range(4) :
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N :
            if map[new_x][new_y] == '1' and not visited[new_x][new_y] :
                visited[new_x][new_y] = True
                dfs(new_x, new_y)

for i in range(N) :
    for j in range(N) :
        if map[i][j] == '1' and not visited[i][j] :
            visited[i][j] = True
            cnt = 0
            dfs(i, j)
            arr.append(cnt)

arr.sort()
print(len(arr))
for count in arr:
    print(count)