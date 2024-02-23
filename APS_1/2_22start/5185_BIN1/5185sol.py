import sys
sys.stdin = open('5185_input.txt')

def dec_to_bin(num):
    if num <= 1:
        return str(num)
    else:
        return dec_to_bin(num // 2) + str(num % 2)
hex_to_dec = {hex(i).replace('0x', '').upper(): i for i in range(16)}

T = int(input())
for tc in range(1, T+1):
    N, hexadecimal = input().split()
    result = ''
    # 16진수 => 10진수 => 2진수
    # print(hex_to_dec)

    for h in hexadecimal:
        # print(hex_to_dec.get(h))
        decimal = hex_to_dec.get(h)
        binary = dec_to_bin(decimal)
        while len(binary) < 4:
            binary = '0' + binary
        # print(binary)
        result += binary

    print(f'#{tc}', result)