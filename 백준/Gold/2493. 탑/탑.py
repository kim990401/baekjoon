N = int(input())
top = list(map(int,input().split()))
stack=[]
ans = [0]*N

for i in range(N) :
    while stack :
        if stack[-1][1] < top[i] :
            stack.pop()
        else :
            ans[i] = stack[-1][0] + 1
            break
    stack.append((i,top[i]))

print(*ans)