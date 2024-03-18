import sys
sys.stdin = open('input.txt')

def partition(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j
    # quicksort(arr, l, j - 1)
    # quicksort(arr, j + 1, r)

def quicksort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quicksort(arr, l, s - 1)
        quicksort(arr, s + 1, r)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    quicksort(arr, 0, len(arr)-1)
    print(f'#{tc}', *arr)
