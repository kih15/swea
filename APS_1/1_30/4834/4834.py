import sys
sys.stdin = open('4834_input.txt')
## 위 줄은 답안 제출할 때 같이 복사 금지

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(input()) # input()하면 그냥 str으로 들어옴. int(input())하는 이유는 int로 변환
    b = list(map(int, a))
    # '0 0 10 20 30' input() => ['0', '0', '10', '20', '30'] list(input()) => [0, 0, 10, 20, 30] list(map(int, a))
    # print(a)
    # print(b) # [4, 9, 6, 7, 9], [0, 8, 2, 7, 1], [7, 7, 9, 7, 9, 4, 6, 5, 4, 3] 를 list로 받음.
    # 가장 많이 적힌 숫자가 무엇인지 그리고 그 숫자가 몇장인지
    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
    result = 0
    counts = [0] * 10
    max_x = b[0]
    # counts 배열에 기록
    for x in b:
        counts[x] += 1
        if x > max_x:
            max_x = x
        elif x == max_x:
            result += 1
    # print(counts) # 인덱스 별 숫자의 개수
    # [0, 0, 0, 0, 1, 0, 1, 1, 0, 2], [1, 1, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 2, 1, 1, 3, 0, 2]
    max_cnt = counts[0]
    max_value = 0
    # 가장 많이 적힌 숫자가 무엇인지? 가장 많이 적힌 숫자가 몇장인지, 카드 장수가 같을 때 큰 숫자가 적힌 카드가 출력되도록
    for index in range(10):
        if counts[index] >= max_cnt: # >= 이 아니라 >로 하면 카드 장수가 같을 때 튕겨나감. >= 으로 하면 장수가 같아도 큰 숫자가 적히도록 출력됨

            max_cnt = counts[index]
            max_value = index

        # print(max_value, max_cnt, "<<<<<<<<<<<<<<<<<<<")

    # 출력!!!
    print(f'#{tc} {max_value} {max_cnt}')