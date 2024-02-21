def quick_sort(target):
    N = len(target)

    if N <= 1:
        return target

    p_idx = N//2    # 처음, 마지막, 중간 어느 것을 선택해도 됨
    pivot = target[p_idx]
    left = []
    right = []

    for idx in range(N):
        if idx == p_idx: continue    # pivot 위치는 제외
        if target[idx] < pivot:
            left.append(target[idx])
        else:
            right.append(target[idx])

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [3, 6, 8, 1, 2, 0, 4, 5, 7, 9]
res = quick_sort(arr)
print(res)
