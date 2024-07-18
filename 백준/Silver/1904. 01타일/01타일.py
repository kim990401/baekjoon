N = int(input())
dp = [1] * (N+1)
for i in range(N+1) :
    if i >= 2 :
        dp[i] = (dp[i-1] + dp[i-2])%15746
print(dp[N]%15746)