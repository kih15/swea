import sys
sys.stdin = open('algo2sample_in.txt')

# def max_v():
#     for k in range(N):
#         for l in range(N):
#             v = A[k][l]
#         if max_v < v:
#             max_v = v
#         return max_v
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # print(A)
    max_v = 0
    v = 0
    s = e = 0
    x = y = -1
    cnt = 0
    while True:
        if s == x and e == y:
            break
        for i in range(M):
            for j in range(M):
                c = e + j
                r = s + i
                if 0 <= c < N and 0 <= r < N:
                    v = A[r][c]
                    if max_v < v:
                        max_v = v
                        x = r
                        y = c
    
        print(x, y)

        # 행렬내 최대값이 이전 최대값의 위치와 동일하다면 break


        # cnt += max_v
        # print(cnt)

    # print(max_v)

