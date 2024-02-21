# arr를 정렬 하는 함수
# 버블정렬, 선택정렬, 카운팅 정렬
# 버블 정렬 : 두 개씩 비교해서 큰 거를 뒤로 보내서 정렬하는 방법.
num_dic = {
    'ZRO' : 0,'ONE' : 1,'TWO' : 2,'THR' : 3,'FOR' : 4,
'FIV' : 5,'SIX' : 6,'SVN' : 7,'EGT' : 8,'NIN' : 9
}

def bubble_sort():
    # 두 개씩 비교해서 큰값을 뒤로 보내는 작업 >> N-1
    for i in range(N-1):
        # 뒤에 값이랑 비교해서 큰값을 뒤로 보내기
        for j in range(N-1-i):
            if num_dic[arr[j]] > num_dic[arr[j+1]]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]

# 선택정렬 : 각 자리에 들어갈 숫자 선택해서 넣어주기
def selection_sort():
    #0번부터 N-2번까지 채워넣기
    for i in range(N-1):    # i번째 칸에 i번째로 작은애 찾아넣기
        # i번째로 작은애 찾기...
        min_idx = i
        for j in range(i+1,N):
            if num_dic[arr[min_idx]] > num_dic[arr[j]]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 카운팅 정렬
# 각 숫자가 몇번씩 나오는지 셈으로서 요소의 위치를 계산하고,
# 그 자리에 요소를 복사
# 제약사항
    # 1. value를 index에 매칭시켜서 개수를 세야하는데...그게 안되면 못씀
    # 2. 정렬 대상의 value의 분포에 따라서 시간이 들쑥 날쑥...
def counting_sort():
    count = [0] * 10    #0~9까지 인덱스가 필요
    sorted_arr = [None] * N # 요소를 정렬하면서 복사할 배열
    # 1. 각 요소가 몇번 나왔는지 세기
    for i in range(N):
        # arr[i] 가 몇번나왔는지 알고 싶음
        # num_dic[arr[i]] : 문자열을 숫자로 바꿈
        count[num_dic[arr[i]]] += 1
    # print(count)
    # 2. 몇 번나왔는지 이용해서 위치 계산(누적합 구하기)
    for i in range(1,10):
        count[i] += count[i-1]
    # print(count)
    # 3. 위치에 맞게 요소 복사하기
    for i in range(N):
        # arr[i] : 얘 위치가 어디있니?
        # ex) SVN 위치를 알고 싶음 count[7]
        count[num_dic[arr[i]]] -= 1 # 순번을 알고 있으니..인덱스를 구하기 위해서 1빼줌
        sorted_arr[count[num_dic[arr[i]]]] = arr[i]
    return sorted_arr




T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    arr = input().split()
    # bubble_sort()
    # selection_sort()
    arr = counting_sort()
    print(tc)
    print(*arr)