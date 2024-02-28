# arr = ['A', 'B', 'C', 'D', 'E']
# n = len(arr)
#
# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end='')
#         tar >>= 1
#
# for tar in range(1 << n):
#     print('{', end= '')
#     get_sub(tar)
#     print('}')
#
# def get_count(tar):
#     cnt = 0
#     for i in range(n):
#         # 1비트 1인지 확인
#         if tar & 0x1:
#             cnt += 1
#         # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
#         tar >>= 1
#     return cnt
#
# result = 0
# for tar in range(1 << n):
#     if get_count(tar) >= 2: # bit가 2개이상 1이라면 -> 2명 이상이라면
#         result += 1
# print(result)

# ABC ABD ABE ACD ACE ADE
# BCD BCE BDE
# CDE

# N = 3
# path = []
#
# def func(lev, start):
#     if lev == N:
#         print(path)
#         return
#     for i in range(start, 7):
#         path.append(i)
#         func(lev+1, i)
#         path.pop()
# func(0, 1)

# arr = {'A': 15, 'B': 30, 'C': 50, 'D': 10}
# n = len(arr)
# for i in range(n):
    # 대기시간이 작은 사람부터

# person = [15, 30, 50, 10]
# n = len(person)
# person.sort()
# sum = 0
# left_person = n - 1 # 화장실을 이용 아직 못한 대기자의 수
#
# for turn in range(n):
#     time = person[turn]
#     # 누적합 = 남은사람 * 시간
#     sum += left_person * time
#     left_person -= 1
#
# print(sum)

n = 3 # 물건 3개
target = 30 # kanpsack 30 kg
things = [(5, 50), (10, 60), (20, 140)] # (kg, price)
# kg당 가격으로 내림차순 정렬
things.sort(key = lambda x : (x[1] / x[0]), reverse= True)

sum = 0

for kg, price in things:
    per_price = price / kg
    # 만약 가방에 남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣고 끝난다.
    if target < kg:
        sum += target * per_price
        break

    sum += price
    target -= kg
print(int(sum))

# 그리디 (회의실 배정)
# 시간이 짧은 회의를 선택한다.
# 다른 회의와 시간이 겹치지 않는 회의를 선택

# 문제 해결 방법
# 회의 종료시간이 가장 빠른 회의부터
# 끝나는 시간을 기준으로 오름차순 정렬
# 빠르게 끝나는 회의를 선택하여 확정
# 이후로 가능한 회의 중, 빠르게 끝나는 회의를 선택하여 확정
