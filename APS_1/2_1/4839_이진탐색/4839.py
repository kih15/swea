import sys
sys.stdin = open('4839_input.txt')

T = int(input())
for tc in range(1, T+1):

    # 이진탐색 연습
    # 먼저 이진탐색을 한 사람은 누구인가?
    # 이진탐색을 적게 실시한 사람이 이긴다. 비긴 경우에는 0을 출력

    def bi_search1(a, key, l, r):   # 함수의 위치는 import 밑에 입력 위에 작성한다.
        count1 = 0                  # 이진탐색의 실시 횟수를 구해야 한다.
        while l <= r:               # while 문이 반복될 때, count1의 횟수가 증가하여야 하므로 while 문 안에 작성.
            count1 += 1
            c = (l + r) // 2
            if a[c] == key:
                return count1       # a[c] == key 일 때, count1(이전탐색의 실시횟수)를 반환
            elif a[c] > key:
                r = c
            else:
                l = c

    def bi_search2(a, key, l, r):   # bi_search1 함수와 bi_search2 함수는 굳이 중복해서 작성할 필요가 없음
        count2 = 0                  # 인자만 바꿔주면 되기 때문에
        while l <= r:
            count2 += 1
            c = (l + r) // 2
            if a[c] == key:
                return count2
            elif a[c] > key:
                r = c
            else:
                l = c

    P, Pa, Pb = map(int, input().split())
    arr = list(range(P+1))
    a = bi_search1(arr, Pa, 1, P)
    b = bi_search2(arr, Pb, 1, P)
    if a < b:
        print(f'#{tc} A')
    elif a == b:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')



