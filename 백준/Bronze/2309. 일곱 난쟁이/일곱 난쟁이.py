A = []
B = 0
for i in range(9) :
    A.append(int(input()))
    B += A[i]
for i in range(0,9) :
    for j in range(i+1,9) :
        if B-A[i]-A[j] == 100 :
            F = A[i]
            G = A[j]
A.remove(F)
A.remove(G)
A.sort()
for i in range(7) :
    print(A[i])