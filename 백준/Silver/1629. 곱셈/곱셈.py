import sys
input = sys.stdin.readline

A, B, C = map(int,input().split())

def divide(A,B,C) :
    if B == 1 :
        return A%C
    else :
        value = divide(A,B//2,C)
        if B % 2 == 0 :
            return (value * value)%C
        else :
            return (value * value * A)%C

print(divide(A,B,C))