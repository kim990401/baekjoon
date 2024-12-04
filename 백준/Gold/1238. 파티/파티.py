import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
N, M, X = map(int,input().split())
route = [[] for _ in range(N+1)]
reverseRoute = [[] for _ in range(N+1)]

for i in range(M) :
    a, b, c = map(int, input().split())
    route[a].append([b, c])
    reverseRoute[b].append([a, c])

def dijkstra(start, graph) :
    distance = [INF] * (N+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q :
        cur_distance, cur_node = heapq.heappop(q)
        if cur_distance > distance[cur_node] :
            continue
        for next_node, next_distance in graph[cur_node] :
            new_distance = cur_distance + next_distance
            if new_distance < distance[next_node] :
                distance[next_node] = new_distance
                heapq.heappush(q, (new_distance, next_node))
    return distance

ans = [0] * (N+1)
goParty = dijkstra(X, route)
goHome = dijkstra(X, reverseRoute)

for i in range(1, N+1) :
    ans[i] += goParty[i] + goHome[i]

print(max(ans))