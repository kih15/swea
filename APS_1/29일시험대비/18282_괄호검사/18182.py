import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = input().strip()
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', -1)