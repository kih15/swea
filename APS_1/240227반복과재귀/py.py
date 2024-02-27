# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for l in range(1, 4):
#                 print(i, j, k, l)

# # 무한 재귀호출
# def main():
#     KFC(0)
#     print('끝')
#
# def KFC(x):
#     KFC(x+1)
#
# def KFC(x):
#     KFC(x+1)
#
# def KFC(x):
#     KFC(x+1)
#
# print(KFC(0))

# def KFC(x):
#     if x == 6:
#         return
#
#     print(x, end = ' ')
#     KFC(x+1)
#     print(x, end = ' ')
#
# KFC(0)
# def main(x):
#     if x == 6:
#         return
#     print(x)
#     x += 1
#     r(x)
#     print(x)
#
# def r(x):
#     x += 1
#     print(x)
#
# print(main(0))

# bracnh = 2
# level = 3

# def KFC(x):
#     if x == 3:
#         return
#
#     for i in range(2):
#         KFC(x+1)
#
# KFC(0)

# 중복 순열
# path = []
#
# def KFC(x):
#     if x == 2:
#         print(path) # 마지막 출력 결과는 기저조건에서 실행해야함
#         return
#
#     for i in range(3):
#         path.append(i)
#         KFC(x+1)
#         path.pop()

# KFC(0)

# path = []
# def KFC(x):
#     if x == 3:
#         print(path)
#         return
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)
#
# path = []
# def KFC(x):
#     if x == 5:
#         print(path)
#         return
#
#     for i in range(1, 5):
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#
# KFC(0)

# 처음 사용하는 숫자라면 Used에 기록을 해준다.
# 그리고 모든 처리가 끝나고 돌아왔다면, Used에 기록을 지워준다.

# path = []
# used = [False, False, False]
#
# def KFC(x):
#     if x == 2:
#         print(path) # 마지막 출력 결과는 기저조건에서 실행해야함
#         return
#
#     for i in range(3):
#         if used[i] == True : continue
#         used[i] = True # 기록
#         path.append(i)
#         KFC(x+1)
#         path.pop()
#         used[i] = False # 삭제
#
# KFC(0)

# path = []
# used = [False, False]
#
#
# def dice(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         if used[i] == True : continue
#         used[i] = True
#         path.append(i)
#         dice(x+1)
#         path.pop()
#         used[i] = False
#
# dice(0)

# path = []
# used = []
# N = 0
#
# def type1(x):
#     if x == N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         type1(x+1)
#         path.pop()
#
# def type2(x):
#
#     if x == N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         if used[i] == True : continue
#         used[i] = True
#         path.append(i)
#         type2(x+1)
#         path.pop()
#         used[i] = False
#
# used = [False for _ in range(7)]
# N, type = map(int, input().split())
#
# if type == 1:
#     type1(0)    # 중복순열 함수
# if type == 2:
#     type2(0)    # 순열 함수

# path = []

# def dice(x, sum):
#     if sum > 10: # 가지치기기
#        return
#
#     if x == 3:
#         if sum <= 10 : # 실제로는 모두 탐색하지만, 출력만 하지 않는 방법
#             print(f'{path} = {sum}')
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         dice(x+1, sum+i)
#         path.pop()
#
#     dice(0, 0)
path = []
def kfc(x):
    if x == 3:
        print(path)
        return


    kfc(x+1)
    kfc(x+1)
    kfc(x+1)
    kfc(x+1)

kfc(0)