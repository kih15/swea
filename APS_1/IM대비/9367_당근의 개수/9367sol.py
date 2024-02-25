import sys
sys.stdin = open('input.txt')

# data에 점점 커지는 당근의 개수의 최대값을 반환
def solve():
    # 1. 변수 하나 선언해서 연속해서 커지는 개수를 셈
    # 1-1 앞 요소랑 비교해서 내가 더 크면 1 증가
    # 1-2 더 작으면 1로 만들어주기, 1로 만들기전에 증가하는 수가 최대인지 확인
    num = 1 # 점점 커지는 개수를 저장할 변수
    # 계산한 값 중에 최대 한 큰 값 찾는건데
    max_num = 1
    for i in range(1, N):
        if data[i] > data[i-1]:
            num += 1
        else:   # 현재 당근이 이전 당근보다 작거나 같을때, 연속이 끊김
            num = 1
    if max_num < num:
        max_num = num
    return max_num
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = solve()
    print(f'#{tc} {result}')