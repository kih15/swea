import sys
sys.stdin = open('sample_input.txt')

def get_count(N):
    cnt = 0
    for y in range(-N, N+1):
        for x in range(-N, N+1):



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # cnt = 0
    # for x in range(-N, N+1):
    #     for y in range(-N, N+1):
    #         if x**2 + y**2 <= N**2:
    #             cnt += 1
    # print(cnt)