N = int(input())
tmp = N
cnt = 0
# a + b = c + d

while True :
    cnt += 1

    a = tmp//10
    b = tmp%10

    new_num = a + b

    c = new_num//10
    d = new_num%10

    ans = b*10 + d
    if ans == N :
        print(cnt)
        break
    else :
        tmp = ans