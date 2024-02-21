import sys
sys.stdin = open('5099_input.txt')

class cQueue:
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.cQ = [0] * (size+1)    # front 위치를 비워두기 위해 +1

    def Qpeek(self):
        return self.cQ[(self.front+1) % len(self.cQ)]   # 원형큐이므로 인덱스 범위를 맞추기 위해 Q 사이즈만큼 나머지 값을 인덱스로 사용

    def is_full(self):
        return self.front == (self.rear+1) % len(self.cQ)

    def is_empty(self):
        return self.front == self.rear

    def enQ(self, value):
        if self.is_full():
            print('FULL')
            return
        else:
            self.rear = (self.rear+1) % len(self.cQ)
            self.cQ[self.rear] = value

    def deQ(self):
        if self.is_empty():
            print('EMPTY')
            return
        else:
            value = self.Qpeek()
            self.front = (self.front+1) % len(self.cQ)
            self.cQ[self.front] = 0
            return value


T = int(input())
for tc in range(1, T+1):
    # N은 화덕의 크기, M은 피자의 개수
    N, M = map(int, input().split())
    pizza_list = list(map(int, input().split()))

    q = cQueue(N)   # 빈 화덕
    # 빈 화덕에 피자 넣기
    for idx in range(N):
        q.enQ([pizza_list[idx], idx+1]) # Queue 에 [치즈양, 피자번호] 를 넣는다.

    p_idx = idx     # 들어간 마지막 피자 index 를 저장
    result = 0      # 마지막으로 나온 피자 번호를 저장
    while not q.is_empty():
        # 피자를 꺼낸다. # (치즈//2)
        pizza = q.deQ()
        pizza[0] = pizza[0] // 2
        result = pizza[1]
        # 피자 치즈를 확인
        # 피자 치즈가 남아 있다면 그대로 enQ
        if pizza[0]:
            q.enQ(pizza)
        # 피자 치즈가 남아있지 않다면 다음 피자 enQ
        else:
            p_idx += 1  # 다음 피자 번호
            if p_idx < M:
                q.enQ([pizza_list[p_idx], p_idx+1])
            # 다음 피자가 없다면 skip
    print(f'#{tc} {result}')