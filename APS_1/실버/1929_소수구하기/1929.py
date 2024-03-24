import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
for i in range(2, N):
    if N % i == 0:
        pass
    else:
        print(i)
    