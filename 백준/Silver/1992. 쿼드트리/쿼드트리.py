N = int(input())
screen = [0] * N
for i in range(N) :
    screen[i] = list(input())
def quad(x,y,n) : 
    basic = screen[y][x]
    for i in range(x,x+n) :
        for j in range(y,y+n) :
            if screen[j][i] != basic :
                print('(',end='')
                quad(x,y,n//2)
                quad(x+n//2,y,n//2)
                quad(x,y+n//2,n//2)
                quad(x+n//2,y+n//2,n//2)
                print(')',end='')
                return
    if basic == '1' :
        return print(1,end='')
    else :
        return print(0,end='')
    
quad(0,0,N)