import sys
sys.stdin = open('input.txt')

def dfs(i):
    visited = [0]*(V+1)
    stack = []
    result = [i]
    visited[i] = 1
    while True:
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                result.append(i)
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    if V in result:
        answer = 1
    else:
        answer = 0
    return answer

T = 10
for tc in range(1, T+1):
    t, E = map(int, input().split()) # t tc의 번호, n은 길의 총 개수
    arr = list(map(int, input().split()))
    V = 99
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        adjl[a].append(b)
    # print(adjl)
    print(f'#{tc} {dfs(0)}')