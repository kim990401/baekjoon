import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
que = deque()

for i in range(N) :
    let = input().split()
    if 'pop' in let :
        if len(que) == 0 :
            print(-1)
        else :
            print(que.popleft())
    elif 'size' in let :
        print(len(que))
    elif 'empty' in let :
        if len(que) == 0 :
            print(1)
        else :
            print(0)
    elif 'front' in let :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[0])
    elif 'back' in let :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[-1])
    else :
        que.append(let[1])            