def solution(triangle) :
    dp = [0 for _ in range(len(triangle))]
    for row in triangle :
        for i in range(len(row)-1,-1,-1) :
            if i == 0 :
                dp[i] = dp[i] + row[i] 
            elif i == len(row) - 1 :
                dp[i] = dp[i-1] + row[i]
            else :
                dp[i] = max(dp[i-1]+row[i],dp[i]+row[i])
    return max(dp)