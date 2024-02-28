import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
            if max_v < cnt:
                max_v = cnt


    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                cnt = 0
            if max_v < cnt:
                max_v = cnt

    print(f'#{tc}', max_v)
