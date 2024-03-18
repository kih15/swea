import sys
sys.stdin = open('5207_input.txt')

def binarysearch(target):
    global cnt
    low = 0
    high = N-1
    cnt = 0
    stack = []
    h = 1
    l = 0
    while low <= high:
        mid = (low + high) // 2

        if A[mid] == target:
            return mid

        elif A[mid] > target:
            high = mid - 1
            stack.append(h)
        else:
            low = mid - 1
            stack.append(l)

        if len(stack) >= 2:
            for i in range(1, len(stack)):
                if stack[i] != stack[i-1]:
                    cnt += 1
                else:
                    cnt = 0
        else:
            cnt += 1
    return -1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    ans = 0
    res = 0
    for i in range(N):
        ans = binarysearch(B[i])
        cnt += 1
    print(f'#{tc}', cnt)
    print(cnt)


