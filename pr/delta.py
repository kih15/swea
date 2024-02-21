di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 5
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
# i = 3
# j = 4
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if  0<=ni<N and 0<=nj<N:
                print(arr[ni][nj], end = ' ')
        print()
# 무작정 네 방향으로 계산을 하면 좌표를 벗어나버림. -1처럼
