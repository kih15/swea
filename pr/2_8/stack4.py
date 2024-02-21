import sys
sys.stdin = open('input1.txt')

def dfs(i):  # 시작 i, 마지막 V
    visited[i] = 1     # 방문표시
    print(i)        # 출력
    # i에 인접하고 방문안한 w가 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] # adjl[i] 행에는 i에 인접인 정점번호를 저장
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    # adjl[n2].append(n1) # 방향이 없는 경우(양방향 이동가능)
visited = [0]*(V+1) # visited, stack 생성 및 초기화
# print(adjl)
result = dfs(1)