import sys
sys.stdin = open('input.txt')

def in_order(T):
    if N >= T:
        in_order(T*2)
        print(c[T], end= '')
        in_order(T*2+1)

T = 10
for tc in range(1, T+1):
    N = int(input()) # 정점의 수
    E = N - 1 # 간선의 수
    c = [0] # 문자들을 집어넣음 [0, 'W', 'F', 'R', 'O', 'T', 'A', 'E', 'S']

    for i in range(N):
        arr = input().split()
        # print(arr)
        c.append(arr[1])
    print()
    print(f'#{tc} ', end= '')
    in_order(1)


