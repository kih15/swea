import sys
sys.stdin = open('5207_input.txt')

def binarysearch(target):
    global cnt
    low = 0
    high = N-1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == target:
            cnt += 1
            return cnt
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0

    for i in range(M):
        cnt += binarysearch(B[i])

    print(f'#{tc}', cnt)


