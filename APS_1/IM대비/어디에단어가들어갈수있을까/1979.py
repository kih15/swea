import sys
sys.stdin = open('input.txt')

# data 안에 단어가 몇개 들어가는 지 반환하는 함수

def solve():
    # 변수하나 만들어서
    # 빈칸(1)을 만나면 1 증가
    # 벽(0)을 만나면 연속된 빈칸이 몇개였는지 확인
    # 길이가 K인 칸의 개수
    result = 0
    for i in range(N):
        # 빈칸의 개수를 세는 변수
        cnt = 0
        for j in range(N):
            if data[i][j] == '1':
                cnt += 1
            else: # 빈칸이 아닌 곳을 만나면
                # 이전에 빈칸의 길이가 K인지 확인
                if cnt == K:
                    result += 1
                cnt = 0 # 연속된 빈칸의 개수 초기화
        # 행 순회가 끝나면 한번 더 검사
        if cnt == K:
            result += 1
    for i in range(N):
        # 빈칸의 개수를 세는 변수
        cnt = 0
        for j in range(N):
            if data[j][i] == '1':
                cnt += 1
            else:  # 빈칸이 아닌 곳을 만나면
                # 이전에 빈칸의 길이가 K인지 확인
                if cnt == K:
                    result += 1
                cnt = 0  # 연속된 빈칸의 개수 초기화
        # 행 순회가 끝나면 한번 더 검사
        if cnt == K:
            result += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [input().split() for _ in range(N)]

    # for row in data:
    #     print(row)
    result = solve()
    print(f'#{tc} {result}')