A = input()
bracket = list(A)
num = 1
stack = []
ans = 0

for i in range(len(bracket)) :
    if bracket[i] == '(' :
        stack.append('(')
        num *= 2
    elif bracket[i] == '[' :
        stack.append('[')
        num *= 3
    elif bracket[i] == ')' :
        if not stack or stack[-1] == '[' :
            ans = 0
            break
        if bracket[i-1] == '(' :
            ans += num
        stack.pop()
        num //= 2
    else :
        if not stack or stack[-1] == '(' :
            ans = 0
            break
        if bracket[i-1] == '[' :
            ans += num
        stack.pop()
        num //= 3

if stack :
    print(0)
else :
    print(ans)