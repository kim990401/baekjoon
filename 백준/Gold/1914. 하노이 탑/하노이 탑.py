def times(n) :
    if n == 1 :
        return 1
    else :
        return times(n-1)*2 + 1
    

def hanoi(move,start,sub,end) :
    if move == 1 :
        print(start, end)
    else :
        hanoi(move-1,start,end,sub)
        print(start, end)
        hanoi(move-1,sub,start,end)


N = int(input())
K = times(N)
print(K)
if N <= 20 :
    hanoi(N,1,2,3)