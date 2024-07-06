import sys
input = sys.stdin.readline

N = int(input())
row = [0] * N
count = 0

def attack(n) :
    for i in range(n) :
        if row[n] == row[i] or abs(row[i] - row[n]) == abs(i - n) :
            return True
    return False

def N_queens(n) : 
    global count
    if n == N :
        count += 1
        return
    else :
        for i in range(N) :
            row[n] = i
            if not attack(n) :
                N_queens(n+1)

N_queens(0)

print(count)