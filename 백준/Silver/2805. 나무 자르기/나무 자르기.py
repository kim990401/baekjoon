import sys
input = sys.stdin.readline

N, M = map(int,input().split())
tree = list(map(int,input().split()))

tree.sort()
sum = 0

start = tree[0]
end = tree[len(tree) - 1]

def tree_height(start, end, M, arr) :
    global sum
    mid = (start + end)//2
    for i in arr :
        if i > mid :
           sum += i - mid
    if sum == M :
        print(mid)
    elif start > end :
        print(end)
    elif sum > M :
        sum = 0
        tree_height(mid + 1, end, M, arr)
    else :
        sum = 0
        tree_height(start, mid - 1, M, arr)

tree_height(0, end, M, tree)