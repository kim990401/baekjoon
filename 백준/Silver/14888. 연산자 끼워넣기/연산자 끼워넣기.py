N = int(input())
A = list(map(int,input().split()))
trans = list(map(int,input().split()))
min_ans = 10**10
max_ans = -(10**10)

def dfs(oper, depth, ans) :
    global min_ans, max_ans

    if oper == 0 :
        ans += A[depth]
    elif oper == 1 :
        ans -= A[depth]
    elif oper == 2 :
        ans *= A[depth]
    elif oper == 3 :
        if ans < 0 :
            ans = -(-ans//A[depth])
        else : 
            ans = ans//A[depth]

    if depth == len(A) - 1 :
        if min_ans > ans :
            min_ans = ans
        if max_ans < ans :
            max_ans = ans
    for i in range(len(trans)) :
        if trans[i] :
            trans[i] -= 1
            dfs(i, depth + 1, ans)
            trans[i] += 1

dfs(-1,0,A[0])

print(max_ans)
print(min_ans)