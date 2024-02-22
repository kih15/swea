# 1. 최소힙 구현
# 2. n개의 값을 저장
# 3. 마지막 노드부터 루트까지 부모 노드를 찾아서 부모노드의 값을 누적
# 4. 값을 출력

# 최소 힙 클래스
import sys
sys.stdin = open('5177_input.txt')

class MinHeap:
    def __init__(self, size):
        self.last = 0
        self.H = [0] * (size+1) # root가 1번 인덱스 부터이기 때문에

    def is_full(self):
        return self.last == len(self.H)
    def is_empty(self):
        return self.last == 0
    def insert(self, value):
        if self.is_full():
            print('Full')
        else:
            # 마지막 위치에 값을 추가
            # 완전 이진 트리이기 때문에
            self.last += 1
            self.H[self.last] = value

            # 최소 힙 조건을 만족하기 위해
            # 만약 비교할 부모가 있다면 아래 반복
                # 자식 노드와 부모 노드의 값을 비교해서
                # 부모 노드가 더 작다면 확정
                # 부모 노드가 더 크다면 자식의 값과 부모의 값을 교환
            child = self.last   # 막 추가된 위치의 값과 비교
            parent = child // 2
            # 만약 비교할 부모가 있다면 아래 반복
            while parent:
                # 부모 노드가 더 크다면 자식의 값과 부모의 값을 교환
                if self.H[parent] > self.H[child]:
                    self.H[parent], self.H[child] = self.H[child], self.H[parent]
                    # 교환된 부모를 다시 자식으로 변경하여 부모가 있는지 또 확인
                    child = parent
                    parent = child // 2
                # 부모노드가 더 작다면 확정 (반복 종료)
                else:
                    break

    # 힙은 항상 root 만 지울 수 있다.
    def pop_root(self):
        if self.is_empty():
            print("Empty")
        else:
            value = self.H[1]
            # root 에 마지막 요소를 이동 (완전 이진트리를 유지하기 위해)
            self.H[1] = self.H[self.last]
            # 마지막 요소 삭제
            self.H[self.last] = 0
            self.last -= 1

            # 최소 힙을 유지하기 위해 부모와 자식 값을 비교
            parent = 1
            # 자식이 존재하면 비교
            child = parent * 2
            while child <= self.last: # 마지막 원소 인덱스보다 작다면 자식이 존재
                # 오른쪽 자식이 있다면 왼쪽 값과 비교
                if parent*2 + 1 <= self.last and self.H[child] > self.H[parent*2+1]:
                    child = parent*2 + 1

                # 부모와 자식 값을 비교
                if self.H[parent] > self.H[child]:
                    self.H[parent], self.H[child] = self.H[child], self.H[parent]
                    parent = child      # 부모 변경
                    child = parent*2    # 새로운 왼쪽 자식
                else:
                    break

            return value
    def get(self, node):
        return self.H[node]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_heap = MinHeap(N)

    for i in range(N):
        min_heap.insert(arr[i])

    # print(min_heap.last)
    # 마지막 노드의 조상 노드의 값의 합
    last = min_heap.last
    # 조상을 찾자
    total = 0
    while last // 2:
        parent = last // 2
        total += min_heap.get(parent)
        last = parent

    print(f'#{tc} {total}')
