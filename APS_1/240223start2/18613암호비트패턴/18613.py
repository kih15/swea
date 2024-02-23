import sys
sys.stdin = open('input.txt')

pat = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4, '110111': 5,
       '001011': 6, '111101': 7, '011001': 8, '101111': 9}
T = int(input())
for tc in range(1, T+1):
    N = input().strip()
    result = ''
    result2 = ''
    for h in N:
        decimal = int(h, base=16)
        result += f'{decimal:04b}'
        result2 = result[len(N)//2:]
    # print(result2) # 받은 문자열을 2진수로 출력
    # 앞에서 3번째부터 7개씩 출력
    ans = []
    for i in range(0, len(result2), 6):
        s = result2[i:i+6]
        # print(s)
        if len(s) == 6:
            ans.append(pat[s])
    print(f'#{tc}', *ans)