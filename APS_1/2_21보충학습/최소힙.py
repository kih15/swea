# 최소 힙
import heapq

# 힙으로 사용할 리스트
hq = []

# 원소를 삽입
for i in range(10, 0, -1):
    heapq.heappush(hq, i) # 힙으로 사용할 리스트, 삽입할 원소

# 원소를 삭제
for i in range(10):
    print(heapq.heappop(hq), end= ' ')
print()

# 응용

hq = []

heapq.heappush(hq, (-4, "4등"))
heapq.heappush(hq, (-1, "1등"))
heapq.heappush(hq, (-3, "3등"))
heapq.heappush(hq, (-2, "2등"))

for i in range(4):
    print(heapq.heappop(hq), end= " ")