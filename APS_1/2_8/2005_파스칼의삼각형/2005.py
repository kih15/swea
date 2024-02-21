import sys
sys.stdin = open('input.txt')

def pascal(row, col):
    if row == col or col == 0:
        return 1
    else:
        return pascal(row-1, col-1) + pascal(row-1, col)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    for row in range(N):
        for col in range(row+1):      # NxN dl skdhaus
            print(pascal(row, col), end=' ')
        print()
