import sys
sys.stdin = open('4831_input.txt')

T = int(input())
for tc in range(1, T+1):
    # K: 최대 이동횟수, N: 종점, M: 충전소 개수
    K, N, M = map(int, input().split())
    # M 개의 충전소
    # hash 접근 set이 list 보다 in 연산자 사용이 유리
    station = list(map(int, input().split())) # 중복되는 충전소가 없기 때문에 set을 사용가능

    # [1, 3, 5, 7, 9]

    # 충전횟수를 저장할 변수
    charge = 0

    # 버스의 이동 변수
    move = K # 버스는 처음에 충전되어 있기 때문에
    # 마지막 충전소의 위치를 저장하는 변수
    last = 0
    while move < N:     # 버스가 종점에 도달하거나 넘어갈 때 까지
        for _ in range(K):  # K만큼 갔기 때문에 K 번 되돌아 오면 된다.
            if move in station:     # 이동한 거리에 충전소가 있다면
                charge += 1
                break       # 뒤로 되돌아갈 필요가 없기에 break
            move -= 1       # 한 칸씩 뒤로 돌아가기
        if last == move:    # 되돌아갔을 때, 마지막 충전소 위치까지 왔다면
            charge = 0      # 더 이상 이동할 수 없음을 의미
            break           # 더 이상 이동하지 않고 반복 종료

        last = move         # 새롭게 찾은 충전소의 위치를 갱신
        move += K           # 다음 충전소를 찾기 위해 최대 이동

    print(f'#{tc} {charge}')