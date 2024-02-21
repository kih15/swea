import sys
from collections import deque
sys.stdin = open('input.txt')

# def deq():
#     global front
#     value = q[front]
#     front = (front + 1) % n
#     return value
# def enq(value):
#     global rear
#     rear = (rear + 1) % n
#     q[rear] = value

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    q = deque()
    q.append(arr[1])


    # n = 8
    # q = arr[:]
    # front = 0
    # rear = 7
    # tmp = []
    # 큐를 써서 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
    # while q[-1] > 0:
    #     front += 1
    #     tmp = arr[front]
    #     for i in range(1, 6):
    #         rear += 1
    #         arr[rear] = tmp-i
    # print(arr)
    # while True:
    #     for i in range(1, 6):
    #         tmp = deq()
    #         enq(tmp - i)
    #
    #         if q[rear] <= 0:
    #             q[rear] = 0
    #             break
    #     if q[rear] == 0:
    #         break
    #     rear += 1
    #     arr[rear] = arr[i] - 1
    #     front += 1
    #     arr[-1] = arr[i-1]
    #     arr[front] = arr[i]

    # print(q)

