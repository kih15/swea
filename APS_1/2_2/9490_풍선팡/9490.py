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
                for l in range(1, arr[i][j]+1): # arr[i][j] 만큼 반복하고 싶으면 di[k], dj[k]의 값을 반복한만큼 곱해주면 됨
                    ni = i + di[k] * l          # range의 범위는 1, arr[i][j]+1 로 해주어야 한다. 0부터 하면 X
                    nj = j + dj[k] * l
                # cnt 의 값만큼 델타 탐색의 범위를 증가시키고 싶다.
                # 반복문을 어떻게 사용해야 할까?
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
                        temp.append(cnt)
            # print(cnt)
    # print(temp)

    max_v = temp[0]
    for i in temp:
        if max_v < i:
            max_v = i
    # print(max_v)
    print(f'#{tc} {max_v}')

