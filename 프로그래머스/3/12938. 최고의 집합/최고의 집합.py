def solution(n, s):
    answer = []
    if n > s :
        return [-1]
    if s%n == 0 :
        for i in range(n) :
            answer.append(s//n)
    else :
        for i in range(n,0,-1) :
            temp = s//i
            s = s - temp
            answer.append(temp)
    return answer