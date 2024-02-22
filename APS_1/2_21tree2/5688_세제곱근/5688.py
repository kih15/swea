import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = round(N ** (1/3), 5)
    # 반올림해준 값이랑 int씌운 값이랑 같다면 그대로 출력
    # 아니면 -1
    if x == int(x):
        print(f'#{tc}', int(x))
    else:
        print(f'#{tc}', -1)
