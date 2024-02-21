import sys
sys.stdin = open('4875_input.txt')


class Stack:
    def __init__(self, size):
        self.top = -1
        self.stack = [0] * size # stack instance

    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        # xkq dl akwlakr dlseprtmdp dnlclgodlTsmswl qlry
        return self.top == len(self.stack) - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print('Full')
            return 0
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print('Empty')
            return 0
        else:
            value = self.peek()
            self.stack[self.top] = 0 # 값 지우기


def find_start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':   # maze 를 int 로 안받았기 때문에 문자열로 받아야함
                return r, c

# 목적이 출구에 도착할 수 있는지 여부 (backtracking)
# DFS: 모든 정점을 방문
def find_path(r, c):
    result = 0  # 도착 여부 저장
    # 시작 위치 부터 델타 탐색
    stack = Stack(N * N)
    stack.push((r, c))
    row, col = r, c
    # result 가 0인 경우는 도착하지 않은 경우
    while not stack.is_empty():  # stack 이 비어있다라는 의미는 더 이상 이동할 수 있는 곳이 없다.
        # 델타 탐색
        for i in range(4):      # 델타 탐색을 위한 반복
            nr = row + dr[i]
            nc = col + dc[i]
            # 이동할 좌표가 미로 범위 내인지 확인, 이동이 가능한 곳인지도 확인
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':  # 이동 가능 범위 내
                if maze[nr][nc] == '3':
                    return 1
                elif maze[nr][nc] == '0':
                    # 이동할 위치를 방문처리
                    maze[nr][nc] = '1'  # 다시 탐색할 수 없도록 '1' 로 변경 (visited 대신)
                    # 되돌아올 위치를 stack에 저장
                    stack.push((r,c))
                    # 이동
                    row, col = r, c
                    break           # 이동한 곳에서 새롭게 델타 탐색을 위해 break
        else:
        # 더 이상 갈 곳이 없다면 stack 에서 pop 해서 탐색을 이어서 진행
            if not stack.is_empty():
                row, col = stack.pop()

    return 0    # 도착할 수 없음 (while에서 stack이 비어있으면 이동할 곳도 없기 때문)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]

    # 델타 탐색을 위한 상,하,좌,우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작 위치를 찾아야됨
    r, c = find_start()
    result = find_path(r, c)

    print(f'#{tc} {result}')
