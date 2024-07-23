import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    N = int(input())
    applicant = []
    for j in range(N) :
        applicant.append(list(map(int,input().split())))
    applicant.sort()
    ans = 0
    target = applicant[0][1]
    for j in range(N) :
        if target >= applicant[j][1] :
            ans += 1
            target = applicant[j][1]

    print(ans)