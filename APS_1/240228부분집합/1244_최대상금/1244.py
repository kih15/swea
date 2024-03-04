import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = list(map(str, input().split()))
    B = int(B)
    # print(A)
    lst = []
    for i in range(len(A)):
        lst.append(int(A[i]))
    print(lst)
    # lst.sort()
    # print(lst)
    for i in range(B):
        arr[i] =
