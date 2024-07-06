N = int(input())
arr = [0] * N
ans = [0] * N

for i in range(N) :
    arr[i] = int(input())

for i in range(N) :
    print(min(arr))
    arr[arr.index(min(arr))] = 1001