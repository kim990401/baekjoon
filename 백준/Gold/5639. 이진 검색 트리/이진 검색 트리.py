import sys
sys.setrecursionlimit(10**9)

tree = []
while True :
    try :
        A = int(input())
        tree.append(A)
    except :
        break

def check(new_tree) :
    if not new_tree :
        return
    mid = new_tree[0]
    left = []
    right = []
    for i in range(1,len(new_tree)) :
        if new_tree[i] > mid :
            right.append(new_tree[i])
        else :
            left.append(new_tree[i])
    check(left)
    check(right)
    print(mid)


check(tree)