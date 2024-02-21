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


size = 20
stack = [0] * size
T = int(input())

for tc in range(1, T+1):
    string = input()
    s = len(string)
    # print(s)

    # 같은 문자가 연속으로 2개 들어가면 pop을 해준다.
    # 어떻게?
    top = -1
    for idx in string:
        # 스택이 비어있는지 확인 비어있으면 push
        # 비어있지 않다면 가장 꼭대기 값과 비교
        # 같다면 pop 다르면 push
        # print(stack)
        if top == -1:
            push(idx)
        else:
            if stack[top] == idx:
                # print(stack[top], idx)
                pop()
            else:
                push(idx)

    print(f'#{tc} {top+1}')





