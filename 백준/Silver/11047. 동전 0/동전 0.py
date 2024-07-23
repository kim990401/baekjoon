N, K = map(int,input().split())
coins = []
for i in range(N) :
    coins.append(int(input()))
coins.sort(reverse=True)
ans = 0
changes = K
for coin in coins :
    ans += K//coin
    K %= coin
    if K == 0 :
        break
print(ans)
