import sys
sys.stdin = open('5185_input.txt')

T = int(input())
arr = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101',
       '1110', '1111']
a = b = c = d = e = f = 0

for tc in range(1, T+1):
    N, S = input().split()
    s = ''
    lst = []
    for i in range(len(S)):
        t = S[i]
        if t.isdigit():
            lst.append(int(t))
        else:
            if 'A' in t:
                a = 10
                lst.append(a)
            if 'B' in t:
                b = 11
                lst.append(b)
            if 'C' in t:
                c = 12
                lst.append(c)
            if 'D' in t:
                d = 13
                lst.append(d)
            if 'E' in t:
                e = 14
                lst.append(e)
            if 'F' in t:
                f = 15
                lst.append(f)

    for i in lst:
        s += arr[i]
    print(f'#{tc}', s)

    # 진수 변환
    # 이런 방법도 가능은 하다고 함
    # print(f'{int("47FE",16):b}')

