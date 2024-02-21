import sys
sys.stdin = open('1209_input.txt')

T = 10
for tc in range(1, T+1):
    Num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)
    N = len(arr)
    sum_1 = 0

    sum_temp = 0
    for i in range(N):  # 행의 합 구하기 i=0일때 j의 열을 다 temp에 더해준다.
        temp = 0        # sum_temp의 최대값의 합을 구해준다.
        for j in range(N):  # i가 1로 바뀌면 다시 반복
            # print(arr[i][j])
            temp += arr[i][j]
        if sum_temp < temp:
            sum_temp = temp
        # print(sum_temp)

    for i in range(N):  # 열의 합 구하기 i=0 일때 j열을 다 더해준다.
        temp = 0
        for j in range(N):
            temp += arr[j][i]
        if sum_temp < temp:
            sum_temp = temp
        # print(sum_temp)

    for i in range(N):  # | 대각선 구하기 | 대각선은 행과 열이 같으므로 배열의 인덱스가 같은 경우이다.
        temp = 0        # 따라서 for문으로 j열을 반복 안해도 된다.
        temp += arr[i][i]
    if sum_temp < temp:
        sum_temp = temp
    # print(sum_temp)

    for i in range(N):  # / 대각선 구하기 / 대각선은 N-1 에서 i만큼 빼주면 된다. (0, N-1), (1, N-2), ... (N-1, 0)
        temp = 0
        temp += arr[i][N-1-i]
    if sum_temp < temp:
        sum_temp = temp
    # print(sum_temp)
    print(f'#{tc} {sum_temp}')