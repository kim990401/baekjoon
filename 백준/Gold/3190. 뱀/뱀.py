from collections import deque

N = int(input())        # 판의 크기
K = int(input())        # 사과 개수
graph = [[0] * N for _ in range(N)]
for i in range(K) :
    x, y = map(int,input().split())
    graph[x-1][y-1] = 2
L = int(input())        # 뱀 방향변환 횟수
direction = dict()
for i in range(L) :
    x, y = input().split()
    direction[int(x)] = y
dx = [1,0,-1,0]
dy = [0,1,0,-1]

x = 0
y = 0
i = 0
cnt = 0
snake = deque()
snake.append([0,0])
graph[0][0] = 1

def turn (a) :
    global i
    if direction[a] == 'L' :
        i = (i - 1)%4
    else :
        i = (i + 1)%4

while True :
    cnt += 1
    x += dx[i]
    y += dy[i]
    if x < 0 or x >= N or y < 0 or y >= N :
        break
    if graph[y][x] == 2 :
        snake.append([x,y])
        graph[y][x] = 1
        if cnt in direction :
            turn(cnt)
        continue
    if graph[y][x] == 1 :
        break
    else :
        snake.append([x,y])
        graph[y][x] = 1
        tail = snake.popleft()
        graph[tail[1]][tail[0]] = 0
        if cnt in direction :
            turn(cnt)

print(cnt)