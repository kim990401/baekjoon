import heapq

N = int(input())

ans = [0] * (N+1)
ans[0] = 1
out_degree = [0 for _ in range(N+1)]
in_degree = [[] for _ in range(N+1)]
in_degree[0] = None
for i in range(N) :
    a = list(map(int,input()))
    for j in range(N) :
        if a[j] == 1 :
            in_degree[j+1].append(i+1)
            out_degree[i+1] += 1

q = []
n = N
for i in range(1,N+1) :
    if not out_degree[i] :
        heapq.heappush(q,-i)
while q :
    cur_node = -heapq.heappop(q)
    ans[cur_node] = n
    for i in in_degree[cur_node] :
        out_degree[i] -= 1
        if not out_degree[i] :
            heapq.heappush(q,-i)
    n -= 1

if 0 in ans :
    print(-1)
else :  
    print(*ans[1:])