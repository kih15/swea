import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    stack = []
    postfix = ''
    p = {'*': 2, '+': 1}
    for tk in fx:
        if tk in '*+':
            while stack and p[tk] < p[stack[-1]]:
                postfix += stack.pop()
            stack.append(tk)
        else:
            postfix += tk

    while stack:
        postfix += stack.pop()

    stack1 = []

    for tk in postfix:
        if tk.isdigit():
            stack1.append(tk)
        elif tk in '*':
            a, b = int(stack1.pop()), int(stack1.pop())
            stack1.append(a*b)
        elif tk in '+':
            a, b = int(stack1.pop()), int(stack1.pop())
            stack1.append(a+b)
    print(f'#{tc}', *stack1)
