import sys
sys.stdin = open('5203_input.txt')


# 한장씩 뽑아서 비교하는데 3장일때부터.
# 연속된 숫자 run 과 같은 숫자 triplet
# arr 에서 1개씩 뽑는다.
def babygin(t):
    for i in range(n):
        if i < 3:
            A[i] = arr[i * 2]
            B[i] = arr[i * 2 + 1]
        else:

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = 12
    n = N//2
    A = [0] * n
    B = [0] * n


