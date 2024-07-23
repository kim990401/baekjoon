import sys
input = sys.stdin.readline
N = int(input())
time = []
for i in range(N) :
    time.append(list(map(int,input().split())))
time.sort(key=lambda time: time[0])
time.sort(key=lambda time: time[1])
ans = time[0][1]
result = 1
for i in range(1,N) :
    if time[i][0] >= ans :
        ans = time[i][1]
        result += 1
print(result)
