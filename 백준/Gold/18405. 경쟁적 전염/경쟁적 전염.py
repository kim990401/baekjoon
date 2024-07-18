from collections import deque
import heapq
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
# N*N 박스, K 바이러스 갯수
box = [[] for _ in range(N)]
for i in range(N) :
    box[i] = list(map(int,input().split()))
S, X, Y = map(int,input().split())
# S = 시간, X = 열, Y = 행

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    heap = []
    for i in range(N) :
        for j in range(N) :
            if box[i][j] :
                heapq.heappush(heap,(box[i][j],i,j,0))
    q = deque()
    while len(heap) > 0 :
        q.append(heapq.heappop(heap))
    while q :
        virus, x, y, second = q.popleft()
        if second == S :
            break
        for i in range(4) :
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N :
                if not box[new_x][new_y] :
                    box[new_x][new_y] = virus
                    q.append((box[new_x][new_y],new_x,new_y,second+1))

bfs()
print(box[X-1][Y-1])