Testcase = int(input())
for i in range(Testcase) :
    N = int(input())
    coin = list(map(int,input().split()))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    for k in coin :
        for j in range(k,M+1) :
            dp[j] += dp[j-k]
    print(dp[M])