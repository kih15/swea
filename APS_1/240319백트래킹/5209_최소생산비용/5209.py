import sys
sys.stdin = open('5209_input.txt')


def f(i, k):
    global min_v
    if i == k:
        s = 0
        for j in range(k):
            s += arr[j][p[j]]
            # print(s)
        if min_v > s:
            min_v = s
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    min_v = 99 * N
    f(0, N)
    # print(p)
    print(f'#{tc} {min_v}')