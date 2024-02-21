import sys
sys.stdin = open('18123_input.txt')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 밑 코드는 수업시간에 배운 것을 활용
    # di, dj는 왼쪽부터 차례로 오른쪽, 아래, 왼쪽, 위쪽의 이웃한 값을 구한다.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    sum_arr = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):      # ni 는 i + di[0], nj 는 j + dj[0]인 경우 i, j+1의 값
                ni = i + di[k]      # 차례로 0~3까지 넣으면 값을 구할 수 있다.
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N: # 여기서 0과 N사이의 값이어야 하는 이유는 인덱스가 - or N보다 커져버리면 배열 밖으로 벗어나기 때문
                    # print(arr[ni][nj], end=' ')
                    sum_arr += abs(arr[i][j] - arr[ni][nj]) # 절대값을 구해주는 함수 abs 사용 / 기준 값에서 우하좌상의 값의 절대값을 sum_arr에 더해준다.
                    # print(abs(arr[i][j] - arr[ni][nj]), end=' ')
    # print(sum_arr)
    print(f'#{tc} {sum_arr}')
