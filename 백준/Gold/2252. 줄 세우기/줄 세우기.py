from collections import deque

N, M = map(int,input().split())
in_degree = [0 for _ in range(N+1)]
out_degree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
in_degree[0] = None
for i in range(M) :
    a, b = map(int,input().split())
    in_degree[b] += 1
    out_degree[a].append(b)

def topology() :
    q = deque()
    for i in range(1,N+1) :
        if not in_degree[i] :
            q.append(i)
    while q :
        a = q.popleft()
        visited[a] = True
        print(a, end=' ')
        for i in out_degree[a] :
            if in_degree[i] :
                in_degree[i] -= 1
                if not in_degree[i] :
                    q.append(i)
    for i in range(1,N+1) :
        if not visited[i] :
            print(i, end=' ')

topology()