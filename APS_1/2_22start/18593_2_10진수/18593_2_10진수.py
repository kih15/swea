import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 비트 문자열의 입력 개수
    tmp = ''
    print(f'#{tc}', end= ' ')
    for i in range(N):
        arr = input().strip()
        tmp += arr
    for i in range(0, len(tmp), 7):
        c = tmp[i:i+7]  # 7글자씩 묶어줌
        cnt = 0
        for j in range(7):
            if c[j] == '1':
                cnt += 2**(6-j)

        print(cnt, end= ' ')


