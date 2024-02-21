import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    stack = []
    postfix = ''
    p = {'*': 2, '/': 2, '+': 1, '-': 1}
    # 후위 표기식으로 바꿔준다.
    for tk in fx:
        if tk in '*/+-':
            while stack and p[tk] < p[stack[-1]]: # p[tk] < p[stack[-1]] 을 stack 이 없는 경우에 비교하면
                                                  # 오류가 발생하므로 stack이 있다고 설정
                # stack.pop() # 같을 때까지 빼내고
                postfix += stack.pop()
            stack.append(tk) # 우선순위가 높으면 push
        else:
            postfix += tk
    while stack:
        postfix += stack.pop()
    # print(postfix)

    stack1 = []

    for tk in postfix:
        if tk not in '*/+-':
            stack1.append(tk)
        elif tk in '*':
            a, b = int(stack1.pop()), int(stack1.pop())
            stack1.append(a * b)
        elif tk in '/':
            a, b = int(stack1.pop()), int(stack1.pop())
            stack1.append(a // b)
        elif tk in '+':
            a, b = int(stack1.pop()), int(stack1.pop())
            stack1.append(a + b)
        elif tk in '-':
            a, b = int(stack1.pop()), int(stack1.pop())
            stack1.append(a - b)
    print(f'#{tc}', *stack1)


