import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_v = 0
    if m > n:
        for i in range(m-n+1):
            total = 0
            for j in range(n):
                total += a[j] * b[i+j]
            if max_v < total:
                max_v = total
    else:
        for i in range(n-m+1):
            total = 0
            for j in range(m):
                total += a[i+j] * b[j]
            if max_v < total:
                max_v = total

    print(f'#{tc} {max_v}')

