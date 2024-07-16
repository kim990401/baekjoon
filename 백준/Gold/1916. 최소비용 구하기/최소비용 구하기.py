import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
cost = [sys.maxsize] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(start):
    q = []
    cost[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        current_cost, current_node = heapq.heappop(q)
        if current_cost > cost[current_node]:
            continue
        for next_node, travel_cost in bus[current_node]:
            new_cost = current_cost + travel_cost
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

dijkstra(start)
print(cost[end])