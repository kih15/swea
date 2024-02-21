import sys
sys.stdin = open('4880_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1은 가위, 2는 바위, 3은 보
    arr = list(map(int, input().split()))
    # 1 < 2, 2 < 3, 1 > 3
