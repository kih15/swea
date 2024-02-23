import sys
sys.stdin = open('5185_input.txt')


hex_to_dec = {hex(i).replace('0x', '').upper(): i for i in range(16)}
T = int(input())
for tc in range(1, T+1):
    N, hexadecimal = input().split()
    result = ''
    for h in hexadecimal:
        # decimal = int(h, base=16)
        decimal = hex_to_dec.get(h)
        result += f'{decimal:04b}'
    print(f'#{tc}', result)