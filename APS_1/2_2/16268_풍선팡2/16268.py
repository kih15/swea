import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    temp = []
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M: # 0<=ni<N and 0<=nj<M으로 해야하는데 0<=ni<N and 0<=nj<N으로 잘못했었음
                    cnt += arr[ni][nj]          # N, M 배열 주의!!
                    temp.append(cnt)
            # print(cnt)
    # print(temp)

    max_v = temp[0]
    for i in temp:
        if max_v < i:
            max_v = i
    # print(max_v)
    print(f'#{tc} {max_v}')