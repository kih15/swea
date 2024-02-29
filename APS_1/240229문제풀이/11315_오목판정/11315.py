import sys
sys.stdin = open('sample_input (1).txt')

# def omok(y, x):
#     dy = [1, 0, 1, -1] # 아래, 오른쪽, 4시방향(대각선), 7시방향(대각선)
#     dx = [0, 1, 1, 1]
#
#     # 네 방향 탐색
#     for bang in range(4):
#         cnt = 1 # 기준 좌표에 돌이 있다. cnt = 1부터 시작
#         # 돌 4개를 탐색
#         for power in range(1, 5):
#             ny = y + (dy[bang] * power)
#             nx = x + (dx[bang] * power)
#             if not (0 <= ny < n and 0 <= nx < n): break
#             # 돌을 발견하면 count
#             if arr[ny][nx] == 'o': cnt += 1
#
#             if cnt == 5: # 오목이다.
#                 return True
#     return False
#
# def game_start():
#     for r in range(n):
#         for c in range(n):
#             if arr[r][c] == 'o':
#                 if omok(r, c):
#                     return 'YES'
#     return 'NO'

T = int(input())
for tc in range(1, T+1):
    # n = int(input())
    # arr = [input() for _ in range(n)]
    # result = game_start()
    # print(f'#{tc} {result}')
    N = int(input())
    arr = [input() for _ in range(N)]
    di = [1, 0, 1, -1]
    dj = [0, 1, 1, 1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if arr[i][j] == 'o':
                    cnt = 1
                else:
                    break
                for l in range(1, 5):
                    ni = i + (di[k] * l)
                    nj = j + (dj[k] * l)
                    if not (0 <= ni < N and 0 <= nj < N): break
                    if arr[ni][nj] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt == 5:
                    print(f'#{tc}', 'YES')
                    break
            if cnt == 5:
                break
        if cnt == 5:
            break
    else:
        print(f'#{tc}', 'NO')

    # 1. 방향 배열
    # 2. 돌 발견 cnt += 1
        # cnt == 5:
            # return True
    # continue를 쓰는 것보다 break가 더 좋은 성능을 낸다.

    # lst = [1, 2, 3, 4, 5]
    # for i in lst:
    #     if i == 3:
    #         continue  # 1 2 4 5 # 반복문의 처음으로 돌아감
    #         # break # 1 2 # 가장 가까운 반복문 탈출/종료
    #     print(i)
