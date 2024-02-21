import sys
sys.stdin = open('input.txt')

top = -1


def push(n):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = n


def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]


T = int(input())
for tc in range(1, T+1):
    string = input()
    # print(string)
    num = len(string)
    size = 30
    stack = [0] * size

    for i in string:
        # print(i)
        if i == '(':
            push(i)
        elif i == ')':
            pop()

    if top == -1:   # top이 -1인 경우가 stack에 남은 자료가 없다.
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {-1}')