import sys
sys.stdin = open('4834_input.txt')
## 위 줄은 답안 제출할 때 같이 복사 금지

T = 10
for tc in range(1, T+1):
    N = int(input())
    box_h = list(map(int, input().split())) # input()하면 그냥 str으로 들어옴. int(input())하는 이유는 int로 변환
