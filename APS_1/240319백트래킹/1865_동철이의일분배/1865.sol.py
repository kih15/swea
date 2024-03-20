import sys
sys.stdin = open('input1.txt')

def perm(person):
    global max_effi
    # 종료 조건
    if person == N:
        # print(work)
        temp = 1
        for w in work:
            temp *= w
        if max_effi < temp:
            max_effi = temp
        return

    # 일을 차례대로 하나씩 맡기
    for i in range(N):
        if used[i]:     # 이미 누가 일을 맡았다면
            continue
        # 맡지 않은 일이 있다면
        used[i] = 1     # 해당 일을 맡음
        work.append(work_list[person][i]*0.01)
        perm(person+1)  # 다음 사람 차례
        work.pop()
        used[i] = 0     # 새로운 일을 맡기 위해 초기화



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work_list = [list(map(int, input().split())) for _ in range(N)]
    work = []   # 임시
    max_effi = 0    # 최대 효율을 저장
    # 해당 일을 맡았는지 확인
    used = [0] * N
    perm(0)
    print(f'#{tc} {max_effi*100:.06f}')