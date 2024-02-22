import sys
sys.stdin = open('input.txt')

code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
        '0110111': 8, '0001011': 9}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    x = y = 0
    for i in range(N-1, -1, -1):
        for j in range(M):
            if arr[i][j] == '1':
                x = i
                y = j
    # print(x, y) # 뒤에서 1을 찾는 좌표 (암호 코드의 시작 위치)
    code_num = arr[x][y-55:y+1] # 암호코드
    # print(code_num)
    tmp = []
    for i in range(0, 56, 7):
        tmp.append(code_num[i:i+7]) # 암호코드를 8개로 나눠준다.
    # print(tmp)
    # 딕셔너리를 활용해서 키로 값을 뽑아줘야하는데...
    s = []
    for i in range(8):
        s.append(code[tmp[i]])
    # print(s)
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        if i % 2 == 0:
            cnt1 += s[i]
        else:
            cnt2 += s[i]
    # print(cnt1*3 + cnt2)
    if (cnt1*3 + cnt2) % 10 == 0:
        print(f'#{tc}', cnt1 + cnt2)
    else:
        print(f'#{tc}', 0)