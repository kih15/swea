import sys
sys.stdin = open('4843_input.txt')

def sp_sort1(a, n):     # 주어진 리스트를 내림차순으로 정렬한다.
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if a[max_idx] < a[j]:
                max_idx = j
        a[max_idx], a[i] = a[i], a[max_idx]
    return


# def sp_sort2(a, n):
#     for i in range(n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         a[min_idx], a[i] = a[i], a[min_idx]
#     return
    # if i % 2 == 0:
    #     sp_sort1(arr, N)
    #     print(arr)

# 인덱스가 짝수일 때 최대값 내림차순
# 인덱스가 홀수일 때 최소값 올림차순
# 10개까지만 출력한다.

# 처음에 내가 해결해려고 했던 생각.
# 오름차순으로 정렬을 한 다음에 if 문을 사용해서
# 인덱스가 짝수랑 홀수인 경우로 나눠서 리스트 안에 집어 넣으려고 했다.
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    sp_sort1(arr, N)
    # print(arr)
    sp_list = []
    # print(sp_list)
# 해결방법: 빈 리스트를 만들고 그 리스트 안에 for 반복문을 사용해서 집어넣었다.
# 오름차순으로 정렬한 후에 앞에 인덱스 5개 뒤에 인덱스 5개를 집어넣었다.
# 굳이 if문을 사용해서 홀수와 짝수로 구분한 후에 할 필요가 없다.
    for x in range(5):
        sp_list.append(arr[x])
        sp_list.append(arr[N-1-x])
    number = ' '.join(map(str, sp_list))
    print(f'#{tc} {number}')

