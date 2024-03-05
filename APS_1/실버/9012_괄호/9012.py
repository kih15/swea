import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input()
    # print(s)
    stack = []
    error = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        # 계속 stack이 있을 때 s[i] == ')'가 stack에 들어오면으로 조건을 설정하니까
        # ')'가 먼저 들어오면 문제가 발생했다...
        if len(stack) > 0 and stack[-1] == '(' and s[i] == ')':
            stack.pop()
        elif s[i] == ')':
            stack.append(s[i])
        # elif len(stack) >= 1 and s[i] == '(':
    # print(stack)
    # 올바른 괄호문자열을 어떻게?
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

