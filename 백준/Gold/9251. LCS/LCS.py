lan_1 = input()
lan_2 = input()

dp = [[0]*(len(lan_1)+1) for _ in range((len(lan_2)+1))]

for i in range(1,len(lan_2)+1) :
    for j in range(1,len(lan_1)+1) :
        if lan_1[j-1] == lan_2[i-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            
print(dp[-1][-1])