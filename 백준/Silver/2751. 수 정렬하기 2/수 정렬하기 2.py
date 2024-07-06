import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N) :
    A.append(int(input()))
A = sorted(A)
for i in range(N) :
    print(A[i])