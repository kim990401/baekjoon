N = int(input())
A = list(map(int,input().split()))
dp = [1] * N

for i in range(N-1) :
    for j in range(i+1,N) :
        if A[i] < A[j] :
            if dp[i] >= dp[j] :
                dp[j] = dp[i]+1
print(max(dp))