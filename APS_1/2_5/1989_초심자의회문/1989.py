import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     a = list(input())
#     # print(a)
#     n = len(a)
#     count = 0
#     for i in range(n):
#         if a[i] == a[n-1-i]:
#             count += 1
#
#         if a[i] != a[n-1-i]:
#             count += 0
#     if count == n:
#         result = 1
#     else:
#         result = 0
#
#     print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T+1):
    words = input()
    temp = ''
    for idx in range(len(words)-1, -1,  -1): # 시작점, 끝값, 줄어드는양
        # [len(words)-1:-1:-1] == [::-1]
        temp += words[idx]
        # 문자열을 더한다
    print(temp)

# T = int(input())
# for tc in range(1, T+1):
#     pal = input()
#     if pal == pal[::-1]:
#         result = 1
#     else:
#         result = 0
#     print(f'#{tc} {result}')
