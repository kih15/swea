import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    M = 8
    arr = [input() for _ in range(M)]

    # print(arr)
    count = 0
    for i in range(M):
        a = arr[i]
        # print(a)
        for j in range(M - N + 1):
            temp = ''
            for k in range(N):
                temp += a[j+k]
            # print(temp)
            if temp == temp[::-1]:
                count += 1
                # print(temp)
    # print(count)
    count2 = 0
    for i in range(M):
        temp = ''
        for j in range(M):
            temp += arr[j][i]
        # print(temp)
        a = temp
        for k in range(M - N + 1):
            temp = ''
            for l in range(N):
                temp += a[l+k]
            # print(temp)
            if temp == temp[::-1]:
                count2 += 1
                # print(temp)
    # print(count2)
    cnt = count + count2
    print(f'#{tc} {cnt}')






