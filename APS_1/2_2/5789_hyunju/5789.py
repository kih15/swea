import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    L1, R1 = map(int, input().split())
    L2, R2 = map(int, input().split())

    temp = [0] * N
    # for i in range(N):
    #     temp.append(i)
    print(temp)


