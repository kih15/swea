import sys
sys.stdin = open('5174_input.txt')

def pre_order(t):
    global cnt
    if t:
        t
        cnt += 1
        pre_order(left[t])
        pre_order(right[t])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)
    par = [0]*(E+2)
    cnt = 0
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p
    c = E+1
    while par[c] != 0:
        c = par[c]
    root = c
    pre_order(N)
    print(f'#{tc} {cnt}')
