import sys
sys.stdin = open('input.txt')

def Test(M):
    tar = M
    for i in range(N):
        if tar & 1 == 0:
            return 'OFF'
        tar = tar >> 1
    return 'ON'

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(bin(M))
    print(f'#{tc}', Test(M))