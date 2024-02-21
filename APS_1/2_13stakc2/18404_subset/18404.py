import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')


def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end= ' ')
        print()
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)


arr = list(map(int, input().split()))
n = len(arr)
bit = [0]*n
f(0, n)
# for i in range(1<<n):
#     lst = []
#     for j in range(n):
#         if i & (1 << j):
#             lst.append(arr[j])
#     result = 0
#     for k in lst:
#         result += k
#     if result == 10:
#         print(lst)

