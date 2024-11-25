from itertools import combinations

X = int(input())

ans = []
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1,11) :
    for j in combinations(num_list, i) :
        num = ''.join(map(str, reversed(j)))
        ans.append(int(num))

ans.sort()

if len(ans) <= X :
    print(-1)
else :   
    print(ans[X])