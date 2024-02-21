# 최대 힙
heap = [0] * 11
# 마지막 원소의 위치
last = 0

# 삽입 연산
def enq(item):
    global last
    last += 1 # 마지막 원소의 한칸 뒤에 넣어야 하니까
    heap[last] = item

    # 원소를 추가하고 나서 (부모노드 > 자식노드) 이 조건을 만족하는지 검사
    # 현재 원소를 자식노드라고 생각하고
    # 비교할 부모노드의 위치를 계산
    c = last
    p = c // 2

    # 부모노드가 존재하고, 부모노드가 자식노드보다 작으면 계속 교환
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 그 위에 있는 부모와 비교를 계속 해야하기 때문에 위치 변경
        c = p
        p = c // 2

# 삭제 연산
def deq():
    global last

    # 루트노드를 삭제할 건데 자리 바꿀거니까 미리 기억
    root = heap[1]

    # 마지막 위치에 있는 노드를 루트 노드 자리로 땡겨온다.
    heap[1] = heap[last]

    # 원소 하나 삭제 했으니 last - 1
    last -= 1

    # 루트로 마지막 원소를 땡겨왔는데
    # 그 원소가 루트가 될 자격이 있나 검사 (부모 > 자식)
    p = 1
    c = p * 2 # 왼쪽 자식

    # 자리 교환
    # 최대 합은 부모노드가 자식노드보다 커야 한다.
    # 부모가 자식보다 작으면 자리를 계속 교환

    # 자식이 존재 하면 비교
    while c <= last:
        # 왼쪽 자식이 있으면 오른쪽 자식도 있나 확인
        # 둘 중에 큰 자식이랑 자리를 교환
        # 오른쪽 자식이 존재하고 오른쪽 자식이 왼쪽 자식보다 큰가?
        if c + 1 <= last and heap[c] < heap[c+1]:
            # 자리 교환할 자식을 오른쪽으로 바꾸자
            c = c + 1

        # 자식이 부모보다 큰가 확인
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c # 자식을 새로운 부모로 생각
            c = c * 2 # 왼쪽 자식을 기준

        else:
            # 부모보다 큰 자식이 없다. => 제자리를 찾음, 반복 종료
            break
    return root


arr = [6, 4, 5, 1, 3, 2, 9, 7, 8, 10]

for i in arr:
    enq(i)

print(heap)
# 힙 정렬
sorted_arr = []

for i in range(10):
    sorted_arr.append(deq())

print(sorted_arr)