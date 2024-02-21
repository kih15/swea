# tc = int(input())  # Test Case가 주어지는 경우
T = 10
for tc in range(1, T+1):  # 총 1개의 test 케이스가 존재
    # # 정수의 개수 N, 구간의 개수 M이 주어진다.
    # a = input() # input은 txt 파일 한 줄 씩 가져온다.
    # b = list(map(int, a))
    # print(a)
    # print(a.split())
    # b = a.split()
    # N, M = map(int, b) # 언패킹

    N = int(input())  # N 가져오기
    arr = list(map(int, input().split()))  # N개의 숫자 리스트로 가져오기
    result = 0
    for i in range(2, N - 2):  # 앞에 2개와 뒤에 2개는 비어 있기 때문
        left2 = arr[i] - arr[i - 2]  # 가운데 집 층수 - 왼쪽 두번째 집
        left1 = arr[i] - arr[i - 1]  # 가운데 집 층수 - 왼쪽 첫번째 집
        right1 = arr[i] - arr[i + 1]  # 가운데 집 층수 - 오른쪽 첫번째 집
        right2 = arr[i] - arr[i + 2]  # 가운데 집 층수 - 오른쪽 두번째 집
        if left2 > 0 and left1 > 0 and right1 > 0 and right2 > 0:  # 이 경우에 가운데 집이 가장 커서 조망 공간 확보
            arr_list = [left2, left1, right1, right2]  # 21 ~ 25 => left2, left1, right1, right2 의 최솟값 구하는 코드
            min_arr_list = arr_list[0]
            for x in arr_list:
                if x < min_arr_list:
                    min_arr_list = x
            result += min_arr_list
    # 로직
    # 알고리즘이 힘들거나 익숙하지 않으면
    # 반드시 주석 적극 활용
    # 주석에 어떤 값이 출력이 되고, 어떤 동작을 작성해야 하는지
    # 동작을 작성할 때는 최대한 세분화 해서 동작을 작성하면 도움
    # 주석이 길어져도 상관 없음
    # 코드 작성에 길을 잃지 않을 정보를 주석에 작성
    # 어떤 코드를 작성해야 할지 모를 때 주석으로 정리
    # 연습장 사서 필기구로 정리하는 것도 추천천

    # 출력!!!
    print(f'#{tc} {result}')