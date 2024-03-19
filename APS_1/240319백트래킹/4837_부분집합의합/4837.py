import sys
sys.stdin = open('4837_input.txt')

def dfs(level):
    global cnt
    if level == len(arr):
        return


    path[level] = arr[level]
    dfs(level+1)
    path[level] = 0
    dfs(level+1)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    arr = []
    temp = []
    for i in range(N):
        arr.append(i+1)
    path = [0] * len(arr)
    dfs(0)
    for i in range(1, len(path)+1):
        if i != 0:
            temp.append(i)
    if sum(temp) == K:

        cnt = 1
    else:
        cnt = 0

    print(f'#{tc}', cnt)