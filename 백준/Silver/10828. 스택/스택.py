import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N) :
    let = input().split()
    if "pop" in let :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif "size" in let :
        print(len(stack))
    elif "empty" in let :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif "top" in let :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])    
    else : 
        stack.append(let[1])