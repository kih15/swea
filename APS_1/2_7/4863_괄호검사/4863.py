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
    # print(len(string))
    size = 35
    stack = [0] * size

    for i in string:
        if i == '(' or i == '{':
            push(i)
        elif i == ')' or i == '}':
            pop()

    if top == -1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')