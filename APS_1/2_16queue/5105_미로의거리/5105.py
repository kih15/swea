import sys
sys.stdin = open('5105_input.txt')


def bfs(s, N):
    q = []
    visited = [[0] * (N+1) for _ in range(N+1)] # 미로에 맞게 visited 배열 설정
    q.append(s)
    visited[s[0]][s[1]] = 1 # start가 튜플이라서 인덱스로 받아줌
    while q:
        r, c = q.pop(0)
        if arr[r][c] == '3':
            return visited[r][c] - 2 # 시작점과 도착점은 해당 안하니까 -2
        # 해당 지점과 해당 지점에서 이동가능한 r, c를 찾자
        for k in range(4): # 미로에 맞는 델타탐색
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1':
                if visited[nr][nc] == 0: # 통로면
                    q.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == '2':
                start = r, c

    print(f'#{tc}', bfs(start, N))

