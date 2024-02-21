T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    temp = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    cnt += arr[ni][nj]  # 맞힌 칸의 상하좌우 4칸의 합을 구했다.

            # print(cnt)
            base = cnt - arr[i][j]      # base 는 상하좌우 네 칸의 점수를 더한 값에서 맞힌 칸의 점수를 -
            # print(base)
            if base < 0:
                base = 0
            if base % 2 == 0 and base != 0:
                base *= 2
            temp.append(base)

    # print(temp)
    max_bonus = temp[0]
    for x in temp:
        if max_bonus < x:
            max_bonus = x
    print(f'#{tc} {max_bonus}')



