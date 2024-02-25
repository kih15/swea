import sys
sys.stdin = open('4875_input.txt')

def find_start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                return r, c

def find_path(row, col):
    global result
    if result:
        return

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

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]


    r, c = find_start()
    result = 0
    find_path(r, c)

    print(f'#{tc} {result}')
