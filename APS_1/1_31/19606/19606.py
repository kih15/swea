import sys
sys.stdin = open('19606_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    sum_x = 0
    sum_y = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                sum_x += arr[i][j]
            if i == (N-1-j):
                sum_y += arr[i][j]

    print(f'#{tc} {sum_x + sum_y - arr[2][2]}')


