import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, B = map(int, input().split())
A = []
for i in range(N) :
    A.append(list(map(int,input().split())))

def matrixSquared(A, B) :
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            for k in range(N) :
                temp[i][j] += A[i][k]*B[k][j]
            temp[i][j] %= 1000
    return temp

def DnC(n, matrix) :
    if n == 1:
        return [[matrix[i][j] % 1000 for j in range(N)] for i in range(N)]
    
    half = DnC(n // 2, matrix)
    half = matrixSquared(half, half)

    if n % 2 == 1:
        half = matrixSquared(half, A)
    return half

for i in DnC(B, A) :
    for j in i :
        print(j, end=" ")
    print("")