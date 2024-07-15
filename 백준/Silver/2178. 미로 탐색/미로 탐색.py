from collections import deque

N, M = map(int,input().split())
maze = []

for i in range(N) :
    maze.append(list(input()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    q = deque()
    q.append([0,0,1])
    while q :
        a, b, cnt = q.popleft()
        if a == N-1 and b == M-1 :
            print(cnt)
            return
        for i in range(4) :
            y = a + dx[i]
            x = b + dy[i]
            if (0 <= y < N) and (0 <= x < M) :
                if maze[y][x] == '1' :
                    maze[y][x] = '0'
                    q.append([y,x,cnt+1])

bfs()