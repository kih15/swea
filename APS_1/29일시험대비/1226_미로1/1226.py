import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    input()
    N = 16
    maze = [list(input()) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = c = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                r, c = i, j
                break

    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((r, c))
    visited[r][c] = 1
    answer = 0

    while q:
        r, c = q.pop(0)

        if maze[r][c] == '3':
            answer = 1
            break

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
                if visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1

    print(f'{tc} {answer}')


