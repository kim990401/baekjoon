N = int(input())
paper = [0] * N

for i in range(N) :
    paper[i] = list(map(int,input().split()))
blue = 0
white = 0

def check(arr, x, y, N) :
    global blue, white
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] :
                check(arr, x, y, N//2)
                check(arr, x+N//2, y, N//2)
                check(arr, x, y+N//2, N//2)
                check(arr, x+N//2, y+N//2, N//2)
                return
    if color == 1 :
        blue += 1
    else :
        white += 1

check(paper, 0, 0, N)
print(white)
print(blue)