import sys
sys.stdin = open('input.txt')


def dfs(i):
    result = [i] # 시작점
    visited = [0] * (V+1)
    stack = []
    visited[i] = 1
    while True:
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                result.append(i) # 노드를 지나갈 때마다 result 에 i를 추가
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return result


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
# print(adjl)
result = dfs(1)
# for i in result:
#     print(i, end='-')
# map(str, result)
ans = '-'.join(map(str, result))  # list 를 str 로 형변환 해준다음에 str 사이에 -를 join 해준다.
print(f'#{1} {ans}')




