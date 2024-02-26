import sys
sys.stdin = open('5176_input.txt')

def in_order(t):
    global num
    if N >= t:
        in_order(t*2)
        node[t] = num
        num += 1
        in_order(t*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = 1
    node = [0] * (N+1)
    in_order(1)
    print(node[1], node[N//2])