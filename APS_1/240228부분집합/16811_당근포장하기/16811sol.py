import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 당근의 개수
    carrots = list(map(int, input().split()))
    carrots.sort()
    min_value = N # 당근의 개수만큼 차이로 초기화

    # 작은 당근을 하나씩 확인하며 상자에 담자!
    small_box = []
    for s in range(N-2):    # 빈 상자가 있으면 안되기에 중간, 큰 상자에 하나씩 보내기 위해 -2
        small_box.append(carrots[s])
        # s < N-1 조건을 만족해야 range 오류가 안남
        # 인덱스를 증가할 땐 out of range 를 조심
        if carrots[s] == carrots[s+1]: # 같은 크기의 당근을 한 상자에 담기
            continue

        if len(small_box) > N//2: # N // 2를 초과한다면 의미 없음
            break

        # 중간 상자에 담을 차례
        medium_box = []
        for m in range(s+1, N-1):   # 작은 상자에 담은 다음 당근 부터 중간상자에 담고, 큰 상자에 넣을 당근 하나 남겨두기
            medium_box.append(carrots[m])
            if carrots[m] == carrots[m+1]:
                continue

            if len(medium_box) > N//2:
                break

            # 나머지 당근들은 전부 큰 상자에 담아준다.
            large_box = carrots[m+1:]
            if len(large_box) > N//2:
                continue # 중간 박스부터 하나 더 담고 나머지를 큰 박스에 넣기 위해 break 가 아니라 continue

            # 여기까지 코드가 실행되면 모든 조건을 만족하는 박스
            print(small_box, medium_box, large_box)
            sm = len(small_box)
            md = len(medium_box)
            lg = len(large_box)
            # 당근의 개수 차이는 (가장 개수가 많은 상자 - 가장 개수가 적은 상자)
            temp_max = max(sm, md, lg)
            temp_min = min(sm, md, lg)
            temp = temp_max - temp_min  # 당근 개수의 차이

            if min_value > temp:
                min_value = temp

    if min_value == N: # 담을 수 없는 경우
        min_value = -1

    print(f'#{tc} {min_value}')