import sys
sys.stdin = open('4874_input.txt')

T = int(input())
for tc in range(1, T+1):
    fx = input().split()
    # fx = input()
    # print(fx)
    # 숫자는 스택에
    # 연산자를 만나면 스택의 숫자 두개를 꺼내 더하고 결과를 다시 스택에 넣는다.
    # '.'은 스택에서 숫자를 꺼내 출력한다.
    # 나눗셈의 경우 항상 나누어 떨어진다.
    top = -1
    stack = [0] * 20

    for tk in fx:
        if tk not in '+*-/.':
            top += 1
            stack[top] = tk
        if tk == '.':
            break
        if tk == '+':
            top -= 2
            if top < -1: # 스택이 1개면 오류
                break

            ans = int(stack[top + 1]) + int(stack[top + 2])
            top += 1
            stack[top] = ans

        elif tk == '*':
            top -= 2
            if top < -1:
                break
            ans = int(stack[top + 1]) * int(stack[top + 2])
            top += 1
            stack[top] = ans

        elif tk == '/':
            top -= 2
            if top < -1 or int(stack[top+2] != 0): # 분모가 0일때 고려
                break
            ans = int(stack[top + 1]) // int(stack[top + 2])
            top += 1
            stack[top] = ans

        elif tk == '-':
            top -= 2
            if top < -1:
                break
            ans = int(stack[top + 1]) - int(stack[top + 2])
            top += 1
            stack[top] = ans

    if top != 0: # 만약 스택이 빈 게 아니면 오류
        print(f'#{tc}', 'error')
    else:
        print(f'#{tc} {stack[top]}')


