import sys
sys.stdin = open('input.txt')

# 기존 순열은 index의 위치와 변경 횟수 동일 (배열의 길이만큼 check 했기 때문)
# 변경횟수가 제한됬기 때문에 모든 배열을 교환 대상으로 봄
# 순열 (원본을 교환)
def perm(time):  # 재귀 도는 횟수 == 숫자를 바꾸는 횟수
    global max_value, cnt
    value = int(''.join(number))
    # 변경 횟수 별로 중복 숫자를 관리해야한다.
    if value in checked[time]:    # 중복 방지 가지치기
        return
    checked[time].add(value)      # 체크된 적이 없으면 등록

    if time == limit:    # 바꾸는 위치가 N만큼 되면 재귀종료 / N: 리스트의 길이
        # print(number)
        # 최대값인지 확인
        # print(int(''.join(number)))

        cnt += 1
        if max_value < value:
            max_value = value
        return

    else:
        # 바꿀 index를 위해 for 하나 추가
        for i in range(N):
            for j in range(i+1, N):  # 자기 자리를 교환 위치로 보면 안되기 때문에(숫자 카드 2개를 교환해야 함)
                number[i], number[j] = number[j], number[i]
                perm(time + 1)
                number[i], number[j] = number[j], number[i]



T = int(input())
for tc in range(1, T+1):
    number, limit = input().split() # int로 받으면 123으로 되니까 int로 받으면 안된다.
    # map(int, input().split()) 을 하게되면 number 가 list로 변환하기 복잡해진다.
    number = list(number)
    limit = int(limit)

    N = len(number)
    max_value = 0
    cnt = 0 # 비교횟수 체크용

    # checked = set() # 중복을 방지하기 위한 세트
    # 횟수별로 중복 가능성 체크
    checked = [set() for _ in range(limit+1)]
    perm(0)

    print(f'#{tc} {max_value}')