import sys
sys.stdin = open('5177_input.txt')

def in_order(t):
    global ans
    if t <= N:
        in_order(t*2)
        for i in range(t):
            h[t] = arr[i]
        ans.append(h[t])
        in_order(t*2+1)
def
# 최소힙
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    h = [0] * (N+1)
    ans = []
    in_order(1)
    print(ans)