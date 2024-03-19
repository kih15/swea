import sys
sys.stdin = open('input.txt')

def preorder(t):
    if t:
        print(t, end=' ')
        preorder(left[t])
        preorder(right[t])

V = int(input())
E = V-1
arr = list(map(int, input().split()))
adjl = []
left = [0] * (V+1)
right = [0] * (V+1)
for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

preorder(1)