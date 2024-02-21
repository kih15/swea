import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    top = -1
    stack = [0] * N
    postfix = ''
    # 후위 표기식으로 바꿔준다.
    for tk in fx:
        if tk in '+':
            top += 1
            stack[top] = tk
        else:
            postfix += tk
    while top > -1:
        top -= 1
        postfix += stack[top+1]

    for tk in postfix:
        if tk != '+': # 피연산자를 stack에 담아준다.
            top += 1
            stack[top] = tk
        else:
            top -= 2 # 필요한 만큼의 피연산자를 스택에서 pop 해야하니까 2개를 pop 해줘야함
            total = int(stack[top+1]) + int(stack[top+2]) # total 변수에 담아주자.
            top += 1 # 빈 스택에 넣어줘야하니까 스택을 하나 추가
            stack[top] = total # 탑에 total 을 담아준다.
    print(f'#{tc} {stack[top]}')