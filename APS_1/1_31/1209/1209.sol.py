import sys
sys.stdin = open('1209_input.txt')

T = 10
for tc in range(1, T+1):
    test_case = input()
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_total = 0
    # 행의 합
    for outer in range(N):
        total = 0       # 행의 합을 구하기 위한 변수
        for inner in range(N):      # 행의 요소를 하나씩 가져오는 반복문
            total += arr[outer][inner]

        # 최대 값인지 확인
        if max_total < total:
            max_total = total

    # 열의 합
    for outer in range(N):
        total = 0
        for inner in range(N):
            total += arr[inner][outer]

        if max_total < total:
            max_total = total

    # 대각선의 합 좌상 -> 우하
    total = 0
    for i in range(N):
        total += arr[i][i]

    if max_total < total:
        max_total = total

    # 대각선의 합 우상 -> 좌하
    total = 0
    for i in range(N):
        total += arr[i][N-1-i]

    if max_total < total:
        max_total = total

    print(f'#{test_case} {max_total}')