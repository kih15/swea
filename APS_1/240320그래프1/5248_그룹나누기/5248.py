import sys
sys.stdin = open('5248_input.txt')

def dfs(s):
    global cnt
    for to in adjl[s]:
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인접리스트
    adjl = [[] for _ in range(N+1)]
    adjm = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        adjl[a].append(b)
        adjl[b].append(a)
        adjm[a][b] = 1
    print(adjl)
    # print(adjm)
    visited = [0] * (N+1)
    path = []
    cnt = 0
    for i in range(1, N):
        dfs(i)
        print(path)
    print(f'#{tc} {cnt}')
    # adjl의 인덱스가 1이상인 경우에 비어있으면 cnt +1
    # path가 있다면, 같은 경우 합쳐서 cnt +1

    # adjl의 경우 인덱스 1부터 보면 되니까.
