import sys
sys.stdin = open('input.txt')

# 열검사 함수
def get_sero_cnt(col):
    cnt = 0
    # red 자성체를 체크
    is_red = False

    for row in range(N):
        # 1. red 자성체 발견
        if arr[row][col] == 1:
            is_red = True
        # 2. 이전에 red 자성체를 발견했고, 현재 blue 자성체 발견 cnt += 1
        elif is_red and arr[row][col] == 2:
            cnt += 1
            is_red = False # 갱신
    return cnt


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_cnt = 0
    # 열 순회하면서 total_cnt 누적
    for col in range(N):
        total_cnt += get_sero_cnt(col)
    print(f'#{tc} {total_cnt}')

    # di = [0]
    # dj = [1]
    # for i in range(N):
    #     for j in range(N):
    #         # 1이 빨강 2가 파랑
    #         if arr[j][i] == 1:
    #             for k in range(1):
    #                 for l in range(N-k):
    #                     ni = i + di[k] * l
    #                     nj = j + dj[k] * l
    #                     if 0 <= ni < N and 0 <= nj < N:
    #                         if arr[nj][ni] == 2:
    #                             cnt += 1
    #             # 다음에 파랑을 만나면
    # print(cnt)
