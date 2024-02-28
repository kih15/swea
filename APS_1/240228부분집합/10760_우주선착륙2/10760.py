import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    # 델타탐색을 이용해서 기준점보다 값이 낮은 장소를 찾아낸다.
    # 예비 후보지의 개수가 4개 이상인 장소의 개수를 구한다.
    result = 0
    for i in range(N):
        for j in range(M):
            place = arr[i][j]
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if place > arr[ni][nj]:
                        cnt += 1
            if cnt >= 4:
                result += 1
            # print(cnt)
    print(f'#{tc} {result}')