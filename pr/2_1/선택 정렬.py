# def selectionSort(a, N): # 오름차순의 선택 정렬
#     for i in range(N-1): # i 주어진 구간의 시작
#         min_idx = i # 맨 앞 원소를 최솟값 위치로 가정
#         for j in range(i+1, N): # 구간 안의 실제 최솟값 위치 검색
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]

def select(arr, k):
    for i in range(0, k):
        minindex = i
        for j in range (i+1, len(arr)):
            if arr[minindex] > arr[j]:
                minindex = j
            arr[i], arr[minindex] = arr[minindex], arr[i]
        return arr[k-1]

K = 4
arr = [1, 3, 2, 5, 4]
print(arr)
select(arr, K)
print(arr)