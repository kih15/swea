import sys
sys.stdin = open('5178_input.txt')

def post_order(t): # 계산을 해야하면 후위표기
    if t <= N:
        post_order(t*2)
        post_order(t*2+1)
        # print(t, leaf[t], end='/')
        if leaf[t] == 0:
            if t*2+1 <= N: # 자식 노드가 둘인 경우
                leaf[t] = leaf[t*2] + leaf[t*2+1]
            else: # 자식 노드가 하나인 경우
                leaf[t] = leaf[t*2]
        # 조건 표현식
        # leaf[t] = leaf[t*2] + leaf[t*2+1] if t*2+1 <= N else 0


T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    leaf = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        leaf[a] = b
    post_order(1)
    print(f'#{tc}', leaf[L])





