import sys
sys.stdin = open('in1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    da = [1, 1, -1, -1]
    db = [1, -1, 1, -1]
    max_v = 0
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            if max_v < cnt:
                max_v = cnt


    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    na = i + da[k] * l
                    nb = j + db[k] * l
                    if 0 <= na < N and 0 <= nb < N:
                        cnt += arr[na][nb]
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')