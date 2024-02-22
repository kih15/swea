N = int(input())
# 윗줄에는 N부터 1씩 증가되는 숫자 4개 왼쪽
# 아랫줄에는 N부터 1씩 감소되는 숫자 4개 오른쪽
# 2*7행렬
arr = [[0] * 7 for _ in range(2)]
t1 = N
for i in range(4):
    arr[0][i] = t1
    t1 += 1

t2 = N
for i in range(6, 2, -1):
    arr[1][i] = t2
    t2 -= 1
print(arr)