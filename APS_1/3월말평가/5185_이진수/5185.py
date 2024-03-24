import sys
sys.stdin = open('5185_input.txt')


T = int(input())
for tc in range(1, T+1):
    N, s = map(str, input().split())
    n = int(N)
    num = ''
    # print(n, s)
    # print(int(s, 16))
    t = int(s, 16)
    # print(bin(t))
    b = bin(t)[2:]
    if len(b) < int(N)*4:
        b = '0'+b
    # print(num)
    # ans = int(num)
    print(f'#{tc} {b}')




