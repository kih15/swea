import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 1
    max_cnt = 0
    for i in range(1, N):
        if C[i-1] < C[i]:
            cnt += 1
        else:
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')
