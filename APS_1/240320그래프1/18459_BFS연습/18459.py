import sys
sys.stdin = open('input.txt')

def bfs(s):
    # 시작점
    q = [s]
    visited[s] = 1

    while q:
        path = q.pop(0)
        print(path, end=' ')

        for to in adjl[path]:
            if visited[to]:
                continue

            visited[to] = 1
            q.append(to)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]
for i in range(E):
    a, b = arr[2*i], arr[2*i+1]
    adjl[a].append(b)
    adjl[b].append(a)
visited = [0] * E
path = []
print(f'#1', end=' ')
bfs(1)
