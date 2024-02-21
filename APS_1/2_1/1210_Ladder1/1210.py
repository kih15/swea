import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    n = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)
    for i in range(N):
        for j in range(N):

                if 0 <= ni < N and 0 <= nj < N:
                    print(arr[ni][nj], end=' ')
            # if arr[i][j] == 1:
            #     arr[i+1][j] = arr[i][j]
            # elif arr[i][j] == 2:
            #     break
            # else: arr[i][j] == 0:
            #
            #         if arr[i][j-1] or arr[i][j+1] == 1:
            #
            #
            #     arr[i][j] = arr[i+1][j]
            #     if arr[i][j] == 2:
            #         return true
            #     elif arr[i][j]
