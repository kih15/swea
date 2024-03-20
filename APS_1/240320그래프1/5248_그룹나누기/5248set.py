import sys
sys.stdin = open('5248_input.txt')

def make_set(x):
    return [i for i in range(x)]

def find_set(x):
    if parents[x] == x:
        return x

    return find_set(parents[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = make_set(N+1)
    # print(parents)
    for i in range(M):
        union(arr[2*i], arr[2*i+1])
    for i in range(1, N+1):
        parents[i] = find_set(i)
    # print(parents)
    # print(set(parents))
    print(f'#{tc}', len(set(parents))-1)