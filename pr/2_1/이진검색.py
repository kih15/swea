def binarySearch(a, N, key):
        strat = 0
        end = N-1
        while start <= end:
                middle = (start + end)//2
                if a[middle] == key : # 검색 성공
                        return true
                elif a[middle] > key:
                        end = middle - 1
                else:
                        start = middle + 1
        return false                # 검색 실패

a = [2, 4, 7, 9, 11, 19, 23]
