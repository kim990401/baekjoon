import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

V, E = map(int,input().split())
spanning = []
parent = [i for i in range(V+1)]
for i in range(E) :
    spanning.append(list(map(int,input().split())))
spanning.sort(key=lambda x : x[2])

def renew_parent(x) :
    if x == parent[x] :
        return x
    return renew_parent(parent[x])

def min_spanning() :
    sum = 0
    E_count = 0
    i = 0
    while E_count < V - 1 :
        a, b, cost = spanning[i]
        x = renew_parent(a)
        y = renew_parent(b)
        if x != y :
            parent[y] = x
            parent[b] = x
            sum += cost
            E_count += 1
            i += 1
        else :
            i += 1
    print(sum)

min_spanning()