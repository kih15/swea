import sys
sys.stdin = open('input.txt')

# 이낮로 받은 num에 각 자리가 3, 6, 9에 해당하는 숫자가 몇 개인지 반환하는 함수
def check(num):
    cnt = 0
    # num을 10으로 나눈 나머지를 확인
    # 몫을 다시 10으로 나눈 나머지를 확인
    # 몫이 0이라면 반복 종료
    while num > 0:
        remain = num % 10
        # remain이 3, 6, 9에 포함되냐
        if remain in [3, 6, 9]:
            cnt += 1
        num = num // 10
    return cnt

N = int(input())
# 1. 1부터 N까지 숫자 출력
# 3, 6, 9를 포함하는 개수만큼 '-' 출력하기
tmp = ['3', '6', '9']
for i in range(1, N+1):
    cnt = check(i)
    num = str(i)
    # num에 3, 6, 9가 몇 개 있는지 검사
    cnt = 0 # 각 숫자에 3, 6, 9,가 몇개 들었는지 검사하는 변수
    # for a in ['3', '6', '9']:
        # cnt += num.count(a)
    # for a in ['3', '6', '9']:
    #     for j in range(len(num)):
    #         if num[j] == a:
    #             cnt += 1
    for i in range(len(tmp)):
        for j in range(len(num)):
            if num[j] == tmp[i]:
                cnt += 1

    if cnt > 0:
        print('-'*cnt, end= ' ')
    else:
        print(num, end= ' ')
#     print(i, end= ' ') # 그냥 출력하는게 아니고
#
# print()