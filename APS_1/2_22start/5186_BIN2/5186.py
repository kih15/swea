import sys
sys.stdin = open('5186_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    s = ''
    i = 1
    while N > 0:
        if N >= 2**(-i):
            N -= 2**(-i)
            s += '1'
        else:
            s += '0'
        i += 1
    if len(s) > 13:
        print(f'#{tc}', 'overflow')
    else:
        print(f'#{tc}', s)
