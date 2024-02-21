import sys
sys.stdin = open('input.txt')

N = int(input())
temp = [] * N
arr = list(map(int, input().split()))
for i in range(N):
    temp.insert(arr[i], i+1)
print(*temp[::-1])