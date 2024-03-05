import sys
sys.stdin = open('input.txt')

import sys
N = int(input())
stack = []
for i in range(N):
    order = list(map(str, sys.stdin.readline().rstrip().split()))
    # print(order)
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'pop':
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()

        else:
            print(-1)



