import sys
sys.stdin = open('input.txt')


N = 5
b = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        print(b[i][j], end=' ')
    print()

c = [list(map(int, input().split())) for _ in range(N+1, N+6)]
temp = []
for i in range(N):
    for j in range(N):
        temp.append(c[i][j])
print(temp)
# temp 리스트에서 하나씩 뽑아서 빙고판의 수를 없앤다.
# 행이나 열을 대각선을 5개 지우면 카운트가 1씩 증가하고
# 3이상 되는 순간 끝난다.
n = len(temp)
count = 0
bingo = 0
for k in range(n):
    for i in range(N):
        for j in range(N):
            if temp[k] == b[i][j]:
                b[i][j] = 0

            print(b[i][j], end=' ')
        print()
