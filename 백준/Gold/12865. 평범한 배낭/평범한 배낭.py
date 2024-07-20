N, K = map(int,input().split())
weight = [None for _ in range(N+1)]
value = [None for _ in range(N+1)]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1,N+1) :
    W, V = map(int,input().split())
    weight[i] = W
    value[i] = V
ans = []
for i in range(1,N+1) :
    a = dp[i-1]
    for j in range(1, K+1) :
        if j < weight[i] :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j-weight[i]]+value[i],dp[i-1][j])
    ans.append(max(dp[i]))

print(max(ans))