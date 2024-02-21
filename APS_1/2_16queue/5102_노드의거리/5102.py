import sys
sys.stdin = open('5102_input.txt')

def bfs(s, N, G):
    q = []
    visited = [0] * (N + 1)
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        if t == G:                  # 도착지점에 도착했으면
            return visited[t] - 1   # 간선 수를 1 빼준다. (처음이 1 이니까)
        for i in adjl[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1
    return 0                        # 두 노드가 연결 되지 않은 경우

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adjl = [[] for _ in range(V + 1)]       # 입력 받을 때 줄줄이로 있으면
    for i in range(E):                      # 반복 돌면서 인접 리스트 만들어준다.
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')

