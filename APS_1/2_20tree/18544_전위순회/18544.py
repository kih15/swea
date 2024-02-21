import sys
sys.stdin = open('input.txt')

def pre_order(T):
    if T:
        print(T, end= ' ')
        pre_order(left[T])
        pre_order(right[T])

V = int(input())
E = V-1
arr = list(map(int, input().split()))
left = [0] * (V+1) # 인덱스 0은 비움, 노드의 수랑 맞춰준다.
right = [0] * (V+1)
par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = V
while par[c] != 0:
    c = par[c]
root = c
pre_order(root)