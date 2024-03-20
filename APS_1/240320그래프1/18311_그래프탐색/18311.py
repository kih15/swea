import sys
sys.stdin = open('input.txt')


def dfs(s):
    for to in adjl[s]:
        if visited[to]:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]
visited = [0] * E
path = []

for i in range(E):
    a, b = arr[2*i], arr[2*i+1]
    adjl[a].append(b)
    adjl[b].append(a)
# print(adjl)
visited[1] = 1
path.append(1)
dfs(1)
ans = '-'.join(map(str, path))
print(f'#1', ans)