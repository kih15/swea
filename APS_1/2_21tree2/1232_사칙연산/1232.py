import sys
sys.stdin = open('input.txt')

def in_order(t):
    global ans
    if t:
        in_order(left[t])
        in_order(right[t])
        ans.append(c[t])


T = 10
for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    c = [0] * (N + 1)
    for i in range(N):
        arr = input().split()
        p = int(arr[0])
        # l = len(arr)
        if len(arr) >= 3:
            left[p] = int(arr[2])
            if len(arr) == 4:
                right[p] = int(arr[3])
        c[p] = arr[1]

    ans = []
    in_order(1)
    # print(ans)
    stack = []
    for i in range(len(ans)):
        if ans[i] not in '*/+-':
            stack.append(ans[i])
        elif ans[i] in '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b + a)
        elif ans[i] in '-':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b - a)
        elif ans[i] in '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b * a)
        elif ans[i] in '/':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b // a)
    print(f'#{tc}', *stack)