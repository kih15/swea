import sys
sys.stdin = open('input.txt')

def dfs(level):
    global cnt
    if level == len(arr):
        # print(path)
        # print(len(set(path)))
        if sum(path) == 0:
        # if len(set(path)) != 1 and sum(path) == 0:
            cnt += 1
        return

    path[level] = arr[level]
    dfs(level+1)
    path[level] = 0
    dfs(level+1)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    path = [0] * len(arr)
    result = 0
    cnt = 0
    dfs(0)
    # print(cnt)
    if cnt >= 2:
        result = 1
    else:
        result = 0

    print(f'#{tc}', result)