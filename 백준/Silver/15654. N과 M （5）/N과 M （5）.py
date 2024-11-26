import itertools

N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

P = itertools.permutations(arr, M)

for i in P :
    for j in i :
        print(j, end=" ")
    print("")