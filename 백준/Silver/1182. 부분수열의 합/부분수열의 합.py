import sys
input = sys.stdin.readline

N, S = map(int,input().split())
list = list(map(int,input().split()))
cnt = 0  

def check(sum,n) :
    global cnt
    for i in range(n,N) :
        check(sum+list[i],i+1)
        if sum+list[i] == S :
            cnt += 1


check(0,0)
print(cnt)
