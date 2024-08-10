

def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    ans = 0
    time = 0
    
    def find(x) :
        while x != parent[x] :
            x = parent[x]
        return x

    for i in costs :
        a = i[0]
        b = i[1]
        count = i[2]
        x = find(a)
        y = find(b)
        if x != y :
            parent[y] = x
            ans += count
            time += 1
        if time == n-1 :
            return ans