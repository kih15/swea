import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    top = -1
    stack = [0] * 20
    icp = {'*': 2, '/': 2, '+': 1}
    isp = {'*': 2, '/': 2, '+': 1}

    fx = input()

    postfix = ''

    # 우선순위가 같을 때 pop 하지 말고 push
    for tk in fx:
        if tk in '*/+':
            if top != -1 and isp[stack[top]] < icp[tk]:
                top += 1
                stack[top] = tk
            elif top != -1 and isp[stack[top]] > icp[tk]:
                while isp[stack[top]] > icp[tk]:
                    top -= 1
                    postfix += stack[top + 1]
            else:
                top += 1
                stack[top] = tk
        else:
            postfix += tk

    while top > -1:
        top -= 1
        postfix += stack[top + 1]

    print(f'#{tc} {postfix}')





