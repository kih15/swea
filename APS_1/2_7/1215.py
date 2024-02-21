import sys
sys.stdin = open('input.txt')


def is_pelindrome(string):
    M = len(string)     # 같은 값이 나오는 함수실행은 한 번만 하면 됨
    # return string == string[::-1]
    for idx in range(M//2 + 1):
        if string[idx] != string[M-1-idx]:
            return False
    return True

T = 10
for tc in range(1, T+1):
    N = 8   # 문자열의 개수
    M = int(input())    # 찾아야 하는 문자열 개수
    arr = [input() for _ in range(N)]   # split()을 하지 않아도 상관없음
                                        # 문자열이고 인덱스 접근이 가능하므로 굳이 추가할 필요 없음
    count = 0   # 회문 개수 세기
    # 행, 열 탐색으로 길이가 M인 문자열을 만들자
    for outer in range(N):
        for inner in range(N-M+1):
            row_str = ''
            col_str = ''
            for idx in range(M):
                row_str += arr[outer][inner+idx]   # 행 문자
                col_str += arr[inner+idx][outer]   # 열 문자

            # 회문인지 판별
            # print(row_str, col_str)
            # if is_pelindrome(row_str):
            #     count += 1
            # if is_pelindrome(col_str):
            #     count += 1
            count += is_pelindrome(row_str) + is_pelindrome(col_str)
    print(f'#{tc} {count}')