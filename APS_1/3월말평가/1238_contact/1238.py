import sys
sys.stdin = open('input.txt')

def bfs(start):
    q = [start]
    visited = [0] * 101
    visited[start] = 1


    # 가장 깊은 depth 의 가장 큰 수
    max_number = start
    # 가장 깊은 depth 를 저장
    max_depth = 1

    while q:
        now = q.pop(0)

        # 갈 수 있는 곳들
        for to in graph[now]:
            # 이미 방문했다면 pass
            if visited[to]:
                continue

            # 현재 방문 = 이전 방문 + 1 번 만에 왔다!
            visited[to] = visited[now] + 1

            # depth 가 더 깊어졌네 ? ==> max_number 초기화
            # depth 는 같은데 숫자가 더 크네? => 초기화
            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to


            q.append(to)

    return max_number


T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    input_graph = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = input_graph[i]
        e = input_graph[i+1]
        graph[s].append(e)

    r = bfs(start)
    print(f'#{tc} {r}')