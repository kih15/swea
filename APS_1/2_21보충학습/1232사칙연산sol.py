import sys
sys.stdin = open('input.txt')

def postorder(t):
    # t번 노드가 숫자면 실수로 바꿔서 리턴한다. (부모노드에서 사용 가능)
    if node[t].isdigit():
        return float(node[t])
    # t번 노드가 연산자면 계산
    else:
        left = postorder(cleft[t])
        right = postorder(cright[t])

        ############################
        if node[t] == "+":
            node[t] = left + right
        elif node[t] == "*":
            node[t] = left * right
        elif node[t] == "-":
            node[t] = left - right
        elif node[t] == "/":
            node[t] = left / right

        return  node[t]
T = 10
for tc in range(1, T+1):
    N = int(input())

    # cleft[p] => p번 노드의 왼쪽 자식 노드 번호
    # cright[p] => p번 노드의 오른쪽 자식 노드 번호
    cleft = [0] * (N+1)
    cright = [0] * (N+1)

    # 피연산자나 연산자를 저장할 배열
    # node[i] => i번 노드에 저장된 연산자 혹은 피연산자
    node = [0] * (N + 1)

    for i in range(N):
        info = input().split()

        # 노드의 번호
        n = int(info[0])

        # 읽어온 줄의 2번째(1번인덱스) 에 있는 글자가 숫자? 연산자?
        if info[1].isdigit():
            # 숫자
            node[n] = info[1]
        else:
            # 연산자
            node[n] = info[1]
            cleft[n] = int(info[2])
            cright[n] = int(info[3])

    print(f"#{tc} {int(postorder(1))}")
