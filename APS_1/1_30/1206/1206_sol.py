import sys
sys.stdin = open('1206_input.txt')

# 양쪽 모두 거리 2 이상의 공간 확보
# 조망권이 확보된 세대의 수를 반환
# 현재 위치를 기준으로 좌, 우 2칸씩
# 빌딩 높이를 확인 (좌, 우측 빌딩의 높이가 가운데보다 낮아야 함)
# 좌, 우 2칸 중 가운데에서 - 가장 높은 빌딩의 높이 => 조망권 확보
# 모든 빌딩을 다 조사를 해야 함
    # 현재 빌딩을 기준으로 좌측 2개, 우측 2개의 빌딩 높이를 조사
    # 4개의 빌딩을 조사할 때, 가장 높은 빌딩을 찾아내면
    # 나보다 높은지 확인하고 낮으면 빼면 됨
    # 뺀 값을 하나의 변수에 누적해 놓고 반환하면 끝!
# 제약 사항
# 가로 최대 길이 1000
# 세로 최대 길이 255
# 맨 왼쪽, 맨 오른쪽 각 두칸은 빌딩이 지어지지 않음 (높이 0)
# 입력
# 총 10개의 t.c
# 첫 줄은 건물의 개수 N
# 다음 줄은 N개의 건물 높이가 주어진다.
# 출력
# 조망권이 확보된 총 세대의 수를 반환

T = 10
for tc in range(1, T+1):
    N = int(input()) # 총 건물의 개수/ 그냥 input을 받으면 문자열이니까 int로 형변환
    building_list =list(map(int, input().split()))  # '0 0 10 20 30' => ['0', '0', '10', '20', '30'] => [0, 0, 10, 20, 30]

    result = 0  # 조망권 개수를 저장하는 변수
    # 모든 빌딩 리스트를 확인해야 함
    # 좌, 우 2칸 씩
    # 인덱스 접근 방식의 반복
    #   -> 좌, 우 2칸씩 접근하려면 요소 반복 보다는 인덱스 반복이 유리
    # building_list 의 길이만큼 range 를 이용하면 됨
    for idx in range(N):
        # building[idx] : idx 현재위치 (현재 빌딩 높이에 접근이 가능)
        # 빌딩을 확인해야 하는데 높이가 0인 것은 확인할 필요가 없음
        if building_list[idx] != 0: # 빌딩 높이가 0인 것은 확인할 필요가 없어서
        # 현재 위치를 기준으로 좌측, 우측 각 2칸씩 높이를 확인할 필요가 있음
            delta_idx = [-2, -1, 1, 2]  # 좌측 2, 좌측 1, 우측 1, 우측 2
        # idx + delta_idx[n] n 번 인덱스 의 위치의 빌딩 높이를 확인할 수 있음
        # building_list[idx + delta_idx[0]] : 좌측 2번째 빌딩의 높이를 알 수 있다.
        # ...
        # building_list[idx + delta_idx[3]] : 우측 2번째 빌딩의 높이를 알 수 있다.
        # 가장 높은 건물을 확인
            max_height = 0
            for n in range(4):  # 4번 반복 (좌, 우 총 4개만 확인하면 되기 때문)
                if max_height < building_list[idx + delta_idx[n]]:  # n번째 빌딩을 확인
                    max_height = building_list[idx + delta_idx[n]]

        # 현재 빌딩의 높이와 가장 큰 빌딩의 높이를 비교
        # 그리고 조망권을 확보할 수 있는지 계산
            if building_list[idx] > max_height:
                result += building_list[idx] - max_height    # 조망권을 누적

    print(f'#{tc} {result}')