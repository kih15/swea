def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        # p 는 기준점의 최종 위치
        quicksort(a, begin, p-1) # 작은 부분
        quicksort(a, p+1, end) # 큰 부분

def quicksort(a, begin, end):
    pivot = (begin + end) // 2 # 어디든 상관없지만 교재의 경우 가운데로 잡음
    L = begin   # 왼쪽 인덱스 인덱스가 증가하면서 기준점까지
    R = end     # 오른쪽 인덱스 인덱스가 감소하면서 기준점까지
    while L < R :   # L=R이 되면 종료
        # 왼쪽 먼저 탐색을 하는데 기준보다 큰 값을 찾을 때까지
        while (L < R and a[L] < a[pivot]): L += 1
            # 탐색조건 / 현재위치 < 기준값   다음요소확인
            # 현재위치가 기준값보다 크다면 왼쪽 탐색 종료
        # 오른쪽 탐색 기준값보다 작은 값을 찾을 때까지
        while (L < R and a[R] < a[pivot]): R -= 1
        if L < R:
            if L == pivot: pivot = R
            a[L], a[R] = a[R], a[pivot]
    a[pivot], a[R] = a[R], a[pivot]
    return R    # 최종 pivot 위치치