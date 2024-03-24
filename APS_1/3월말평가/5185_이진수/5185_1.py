import sys
sys.stdin = open('5185_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, s = map(str, input().split())
    n = int(N)
    t = int(s, 16)
    b = bin(t)[2:]
    if len(b) < n * 4:
        b = '0' + b
    print(f'#{tc} {b}')