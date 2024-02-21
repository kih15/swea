import sys
sys.stdin = open('18124_input.txt')

T = int(input())
for tc in range(1, T+1):

    def f(arr, n):
        for i in range(1, 1 << n):  # 인덱스가 0일때, 공집합이므로 s의 초기값을 0으로 설정하면
            s = 0                   # 결과는 무조건 1로 return 따라서 range의 범위를 1부터
            for j in range(n):
                if i & (1 << j):
                    s += arr[j]
                    # print(arr[j], end = ' ')
            if s == 0:
                return 1
        return 0


    arr = list(map(int, input().split()))
    n = len(arr)
    print(f'#{tc} {f(arr, n)}')