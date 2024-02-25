import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    max_v = 0
    if M > N:
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += int(arrA[j]) * int(arrB[i+j])
            if max_v < total:
                max_v = total
    else:
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += int(arrA[i+j]) * int(arrB[j])
            if max_v < total:
                max_v = total

    print(f'#{tc} {max_v}')


    #     a = 0
    #     for j in range(M-N+1):
    #         a = arrA[i] * arrB[j]
    #         print(a)
    # s = 0
    # for i in range(N):
    #     s = arrA[i:i+M-N+1] * arrB[i]
    #     print(s)
    # # if N > M:
    #     for i in range(N-M+1):
    #         a = arrA[i:i+2]
    #         print(a)
    # a = ''
    # if N < M:
    #     for i in range(M-N+1):
    #         a += arrB[i:i+M-N+1]
    #     print(a)
    # lstA = [0] * M
    # lstB = [0] * N
    # # N이 큰 경우, M을 움직이면서 최대값을 구한다.
    # if N > M:
    #     for i in range(N):
    #         lstB[i] = arrB
    # # M이 큰 경우, N을 움직이면서 최대값을 구한다.

