import sys

def bellman_ford(start) :
    INF = sys.maxsize
    cost = [INF for _ in range(N+1)]
    cost[start] = 0
    for i in range(N+1) :
        for j in range(len(road)) :
            cur_node = road[j][0]
            next_node = road[j][1]
            next_cost = road[j][2]
            if cost[next_node] > cost[cur_node] + next_cost :
                cost[next_node] = cost[cur_node] + next_cost
                if i == N:
                    return True
    return False

Testcase = int(input())

for i in range(Testcase) :
    N, M, W = map(int,input().split())
    road = []
    for j in range(M) :
        S, E, T = map(int,input().split())
        road.append([S, E, T])
        road.append([E, S, T])
    for j in range(W) :
        S, E, T = map(int,input().split())
        road.append([S, E, -T])

    if bellman_ford(1) :
        print("YES")
    else :
        print("NO")