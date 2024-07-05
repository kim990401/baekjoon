def prime_num(n) :
    num = 0
    for i in range(2,n) :
        if n%i == 0 :                #소수가 아닐 경우 num + 1
            num += 1            
            break
    if num == 0 :                    #소수일 경우 num = 0 이므로 return 그대로
        return n
    else :
        return 0                     #소수가 아닐 경우 return 0

TestCase = int(input())

for i in range(TestCase) :
    n = int(input())
    a1 = n//2                        #입력값의 중간부터 서치
    while True :
        if prime_num(a1) == 0 :
            a1 -= 1                  #a1이 소수가 아닐경우 a1 - 1 하고 다시 서치
        else :
            a2 = n - a1              #a1이 소수 일 경우 a2 서치
            if prime_num(a2) == 0 :
                a1 -= 1              #a2가 소수가 아닐경우 a1 - 1 하고 다시 서치
            else : 
                break
    print(a1, a2)
