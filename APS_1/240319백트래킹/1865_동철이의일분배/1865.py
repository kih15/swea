import sys
sys.stdin = open('input1.txt')

def dfs(level):
    if level == len(p):
        print(path)
        return
    for i in range(len(p)):
        if p[i] in path:
            continue
        path[level] = p[i]
        dfs(level + 1)
        path[level] = 0
        # dfs(level + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    # print(p)
    path = [0] * len(p)
    dfs(0)
    per = 0
    print(per)

# def f(i, k):
#     global max_v
#     if i == k:
#         s = 1
#         for j in range(k):
#             s *= arr[j][p[j]]
#         # print(s)
#         if max_v < s:
#             max_v = s
#             return
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     p = [i for i in range(N)]
#     max_v = 0
#     f(0, N)
#     # print(p)
#     print(f'#{tc}', round(max_v, 6))