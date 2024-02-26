import sys
sys.stdin = open('sample_input.txt')

def get_result():
    a = 0
    b = (len(arr) + 1) // 2

    for turn in range(len(arr)):
        if turn % 2 == 0:
            print(arr[a], end=' ')
            a += 1
        else:
            print(arr[b], end=' ')
            b += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    print(f'#{tc}', end=' ')
    get_result()
    print()
    # a = (arr[0])
    # b = (arr[N//2 + 1])
    # for i in range(N):
    #     a += 1
    #     b += 1
    # print(arr)
    # 투포인트 알고리즘
    # a = 맨 처음
    # b = 중간 + 1

    # loop{
#       a 출력 후 a += 1
#       b 출력 후 b += 1
# }