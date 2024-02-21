import sys

# sys.getsizeof()
a = []
print(sys.getsizeof(a))
a.append(1)
print(sys.getsizeof(a))
a.append(2)
print(sys.getsizeof(a))
a.append(3)
print(sys.getsizeof(a))
a.append(4) # 숫자 4개 정도의 메모리 여유를 가지고 확장한다.
print(sys.getsizeof(a))
a.append(5)
print(sys.getsizeof(a))