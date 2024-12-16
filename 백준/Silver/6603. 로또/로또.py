from itertools import combinations
while True :
    T = list(map(int, input().split()))
    if T == [0] :
        break
    T.pop(0)
    for i in combinations(T, 6) :
        print(*i)
    print("")