import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

N, M, X = map(int, input().split())
route = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    route[a].append((b, c))

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cur_distance, cur_node = heapq.heappop(q)
        if cur_distance > distance[cur_node]:
            continue
        for next_node, weight in route[cur_node]:
            new_distance = cur_distance + weight
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(q, (new_distance, next_node))
    return distance

# X에서 모든 노드로 가는 거리
to_X = dijkstra(X)

# 모든 노드에서 X로 가는 거리
max_time = 0
for i in range(1, N+1):
    if i != X:
        from_i = dijkstra(i)
        max_time = max(max_time, from_i[X] + to_X[i])

print(max_time)