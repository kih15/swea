import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    # 2는 푸른색 N극에 끌림
    # 1은 붉은색 S극에 끌림
    di = [0, 0]
    dj = [1, -1]
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    lst = []
    # 1은 아래로 한칸씩 내려감
    # 2는 위로 한칸씩 올라감
    # 만약 1과 2가 부딪히면 멈춤
    # 2가 맨 윗줄에 있으면 0으로 바꿔주고
    # 1이 맨 아랫줄에 있으면 0으로 바꿔준다.
    # 만약
    ot = []
    for i in range(N):
        tmp = ''
        for j in range(N):
            lst = arr[j][i]
            if lst != 0:
                tmp += str(lst)
        ot.append(tmp)
        # print(tmp)
    print(ot)



