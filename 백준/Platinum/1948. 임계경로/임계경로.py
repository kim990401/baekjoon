import sys
import heapq
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
back = [[] for _ in range(N+1)]
cost = [0] * (N+1)
visited = [False for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))
    back[b].append((a, c))
    cost[b] += 1
start, end = map(int, input().split())
 
# 도시별 최대 시간
max_time = [0]*(N+1)
 
# Topological Sort
deq = deque([start])
while deq:
    s = deq.popleft()
    
    for e, t in bus[s]:
        cost[e] -= 1
        # 도시별 최대 도달 시간 갱신
        max_time[e] = max(max_time[e], max_time[s] + t)
        if cost[e] == 0:
            deq.append(e)

max_cost = max_time[end]
cnt = 0
def count_check(end, max_cost) :
    global cnt
    for next_node, next_cost in back[end] :
        if max_cost - next_cost == max_time[next_node] :
            cnt += 1
            if next_node == start :
                return
            if not visited[next_node] :
                visited[next_node] = True
                count_check(next_node, max_time[next_node])

count_check(end, max_cost)
print(max_time[end])
print(cnt)