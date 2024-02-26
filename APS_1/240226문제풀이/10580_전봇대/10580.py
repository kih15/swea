import sys
sys.stdin = open('input.txt')

def get_result():
    # 리스트 arr : 튜플 형태로 a전봇대와 b전봇대를 저장할 리스트
    size = len(arr)
    cnt = 0
    for i in range(size):
        for tar in range(i):
            # a 전봇대 : 튜플의 첫번째 요소, b 전봇대 : 튜플의 두번째 요소
            i_a, i_b = (arr[i][0], arr[i][1])
            tar_a, tar_b = (arr[tar][0], arr[tar][1])
            if i_b < tar_b:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        a, b = map(int, input().split())
        # 튜플 형태로 a전봇대와 b전봇대를 append
        arr.append((a, b))

    arr.sort(key = lambda x : x[0]) # 첫 번째 원소를 기준으로, 오름차순 정렬
    result = get_result()
    print(f'#{tc} {result}')


    # cnt = 0
    # max_v = 0
    # for i in range(N):
    #     a, b = map(int, input().split())
    #
    #     if max_v < b:
    #         max_v = b
    #     if b < max_v:
    #         cnt += 1
    # print(f'#{tc} {cnt}')