import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    f = 0
    for i in range(N):
        for j in range(N):
            f += arr[i:i+2][j]
            if i+2 < N:
    print(f)