import sys
input = sys.stdin.readline

# def lenSort(word) :
#     for i in range(0,len(word)-1) :
#         for j in range(i+1,len(word)) :
#             if len(word[i]) > len(word[j]) :
#                 word[i], word[j] = word[j], word[i]

# def wordSort(word) :
#     for i in range(len(word)-1,0,-1) :
#         for j in range(0,i) :
#             if word[i] < word[j] :
#                 word[i], word[j] = word[j], word[i]
#     return

N = int(input())

word = [0] * N
for i in range(N) :
    word[i] = input().strip()

word = list(set(word))

word = sorted(word)
word.sort(key=len)
for i in word :
    print(i)