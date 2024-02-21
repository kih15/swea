import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # arr = [(input().split()) for _ in range(N)]
    arr = [input() for _ in range(N)]
    temp = ''
    for x in range(N):
        # print(arr[i])
        a = arr[x]
        for k in range(N - M + 1):
            temp = ''
            for l in range(M):
                temp += a[l + k]
            print(temp)
            if temp == temp[::-1]:
                print(f'#{tc} {temp}')
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += arr[j][i]
        # print(temp)
        a = temp
        for k in range(N - M + 1):
            temp = ''
            for l in range(M):
                temp += a[l + k]
            # print(temp)
            if temp == temp[::-1]:
                print(f'#{tc} {temp}')


