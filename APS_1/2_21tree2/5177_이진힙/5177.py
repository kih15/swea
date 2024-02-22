import sys
sys.stdin = open('5177_input.txt')

def enq(item):
    global last
    last += 1
    h[last] = item
    c = last
    p = c // 2
    # 부모노드가 존재하고, 부모노드가 자식노드보다 작으면
    while p and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2

# 최소힙
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    h = [0] * (N+1)
    last = 0

    for i in range(N):
        enq(arr[i])

    result = 0
    i = N
    while i > 0:
        i //= 2
        result += h[i]
    print(result)



