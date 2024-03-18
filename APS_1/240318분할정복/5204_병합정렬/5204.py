import sys
sys.stdin = open('5204_input.txt')

# 분할
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    mid = len(arr) // 2
    for i in range(mid):
        left.append(arr[i])
    for j in range(mid, len(arr)):
        right.append(arr[j])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# 병합
def merge(left, right):
    global cnt
    result = []
    i = 0
    j = 0

    # 오른쪽 원소가 먼저 복사되는 경우의 수를 구해야 된다.
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우
    # left[i] < right[j]
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1


        elif len(left) > i:
            result.append(left[i])
            i += 1
        elif len(right) > j:
            result.append(right[j])
            j += 1

    if left[-1] > right[-1]:
        cnt += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(arr)
    print(f'#{tc}', ans[N//2], cnt)