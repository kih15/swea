import sys
sys.stdin = open('4835_input.txt')
## 위 줄은 답안 제출할 때 같이 복사 금지

T = int(input())
for tc in range(1, T+1):
    N, M = (map(int, input().split())) # N = 정수의 개수, M = 구간의 개수
    arr = list(map(int, input().split()))
    # print(arr)

    temp = []
    for i in range(len(arr)):
        sum_arr = 0
        if i+M <= N:                # 구간의 개수가 M 보다 적어지는 것 방지
            s_arr = arr[i:i+M]      # arr 의 i, i+M-1까지의 개수를 s_arr 에 할당한다.
            # print(s_arr)
            for j in s_arr:         # s_arr 리스트의 합을 더한 값 sum_arr 을 temp 리스트에 추가한다.
                sum_arr += j        # sum_arr 의 초기값은 for 문 안에 작성한다.
            temp.append(sum_arr)
    # print(temp)
            # print(sum_arr)

    max_temp = temp[0]      # max_temp 와 min_temp 의 초기값 설정은 리스트의 첫번째로 설정해준다.
    min_temp = temp[0]
    for i in temp:
        if max_temp < i:
            max_temp = i
    # print(max_temp)
    for j in temp:
        if min_temp > j:
            min_temp = i
    # print(min_temp)

    print(f'#{tc} {max_temp-min_temp}')