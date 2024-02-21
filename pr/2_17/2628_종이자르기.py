import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split()) # 가로, 세로
n = int(input()) # 칼로 자른 수
arr = [[0] * a for _ in range(b)]
tmp = []
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0:
        tmp.append(y)
for i in range(b):
    if i in tmp:
        print(i)

        #
    # else:
    #     tmp_b.append(y)
# print(tmp_a)
# print(tmp_b)
# for i in range(len(tmp_a)):
#     aa = tmp_a[i]
#     max_a = 0
#     if aa < a // 2:
#         if max_a < aa:
#             max_a = aa
#     else:
#         if max_a > a - aa:
#             max_a = a - aa
#     width = max_a
# for i in range(len(tmp_b)):
#     bb = tmp_b[i]
#     max_b = 0
#     if bb < a // 2:
#         if max_b < bb:
#             max_b = bb
#     else:
#         if max_b < b - bb:
#             max_b = b - bb
#     height = max_b
#
#
#
# ans = width * height
#     print(ans)
