import sys
sys.stdin = open('input.txt')

def bfs(s, N):
    q = []
    visited = [[0] * (N+1) for _ in range(N+1)]
    q.append(s)
    visited[s] = 1
    while q:
        r, c = q.pop(0)
        if arr[r][c] == '3':
            return 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
                if visited[nr][nc] == 0:
                    q.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1
    return 0



T = 10
for tc in range(1, T+1):
    M = int(input())
    N = 16
    arr = [list(input().split()) for _ in range(N)]
    # start = (1, 1) end = (13, 13)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    result = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '2':
                start = r, c
    print(start)
    # print(bfs(start, N))