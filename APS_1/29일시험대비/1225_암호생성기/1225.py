import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    q = list(map(int, input().split()))
    i = 1
    while True:
        if i > 5:
            i = 1
        t = q.pop(0)-i
        if t <= 0:
            q.append(0)
            break
        q.append(t)
        i += 1
    print(f'#{tc}', *q)