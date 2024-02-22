import sys
sys.stdin = open('input.txt')

N = int(input())
tmp = ['3', '6', '9']
for i in range(1, N+1):
    num = str(i)
    cnt = 0
    for j in range(len(num)):
        for k in range(len(tmp)):
            if num[j] == tmp[k]:
                cnt += 1
    if cnt > 0:
        print(cnt*'-', end= ' ')
    else:
        print(num, end= ' ')