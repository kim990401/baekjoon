import sys
input = sys.stdin.readline
N = int(input())
dp = [[] for _ in range(N)]
stair = [0] * N
for i in range(N) :
    stair[i] = int(input())
if N == 1 :
    print(stair[0])
else :
    dp[0] = [stair[0],0]
    dp[1] = [stair[0]+stair[1],stair[1]]
    for i in range(2,N) :
        one_step = dp[i-1][1]+stair[i]
        two_step = max(dp[i-2])+stair[i]
        dp[i] = [one_step,two_step]
    print(max(dp[N-1]))