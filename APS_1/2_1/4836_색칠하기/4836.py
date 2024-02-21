import sys
sys.stdin = open('4836_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1, c1, r2, c2, color = map(int, input().split())
    # color = 1 (빨강) color = 2 (파랑)
# 칠이 끝난 후 색이 겹쳐 보라색이 된 칸수를 구하시오.
    arr = [list([0] * 10) for _ in range(10)]
    for x in arr[]