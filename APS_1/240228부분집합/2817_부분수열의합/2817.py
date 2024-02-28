import sys
sys.stdin = open('sample_input.txt')

def get_sub(tar):
    for i in range(N):
        if tar & 0x1:
            print(A[i], end='')
        tar >>= 1

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for tar in range(1 << N):
        print('{', end='')
        get_sub(tar)
        print('}')