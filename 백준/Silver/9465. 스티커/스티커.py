T = int(input())
for i in range(T) :
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    dp1 = [0]*n
    dp2 = [0]*n
    if n == 1 :
        print(max(A[-1],B[-1]))
    else :
        dp1[0] = A[0]
        dp2[0] = B[0]
        dp1[1] = B[0]+A[1]
        dp2[1] = A[0]+B[1]
        for j in range(2, n) :
            dp1[j] = max(dp2[j-2]+A[j], dp2[j-1]+A[j])
            dp2[j] = max(dp1[j-2]+B[j], dp1[j-1]+B[j])
        print(max(dp1[-1],dp2[-1]))
        