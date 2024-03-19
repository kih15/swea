import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
cnt = 0
path = [0] * len(arr)

def dfs(level):
    global cnt
    # 원소의 합이 0이되는 부분집합의 개수

    if level == len(arr):
        if sum(path) == 0:
            cnt += 1
        return

    # for i in range(level, len(arr)):
    #     if arr[i] in path:
    #         continue
    path[level] = arr[level]
    dfs(level + 1)
    path[level] = 0
    dfs(level + 1)

dfs(0)
print(f'#1', cnt)
