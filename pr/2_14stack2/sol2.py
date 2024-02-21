import sys
sys.stdin = open('input.txt')


def find_start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':   # maze 를 int 로 안받았기 때문에 문자열로 받아야함
                return r, c

def find_path(row, col):
    global result
    if result:      # 이미 도착한 경우
        return

    # 델타 탐색
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
            if maze[nr][nc] == '3':
                result = 1
                return
            elif maze[nr][nc] == '0':
                maze[nr][nc] = '1'
                find_path(nr, nc)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]

    # 델타 탐색을 위한 상,하,좌,우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작 위치를 찾아야됨
    r, c = find_start()
    result = 0
    find_path(r, c)

    print(f'#{tc} {result}')