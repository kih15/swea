import sys
sys.stdin = open('input.txt')

K, N = map(int, input().split())
arr = []
for _ in range(K):
    line = int(input())
    arr.append(line)
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in arr:
        num += i//mid
    if num >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)


# 각 랜선 별로 몫(랜선의 길이)을 구한다.
# 랜선이 11개인 경우에 랜선의 최대 길이를 출력한다.
