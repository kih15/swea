import sys
sys.stdin = open('input')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        # print(arr[i][j]) # 행 우선 순회
        # print(arr[j][i]) # 열 우선 순회
        # print(arr[i][j+(N-1-2*j)*(i%2)])
