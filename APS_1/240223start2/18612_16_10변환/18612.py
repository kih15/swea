import sys
sys.stdin = open('input.txt')

hex_to_dec = {hex(i).replace('0x', '').upper(): i for i in range(16)}
T = int(input())
for tc in range(1, T+1):
    S = input().strip()
    h = ''
    # decimal = int(S, 16)
    for i in S:
        decimal = hex_to_dec.get(i)
        # print(decimal)
        h += f'{decimal:04b}'
    print(f'#{tc}', end= ' ')
    for i in range(0, len(h), 7):
        print(int(h[i:i+7], 2), end= ' ')
