import sys
sys.stdin = open('input.txt')

N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
print(a)
for i in range(len(a), 0, -1):
    print(a[i])