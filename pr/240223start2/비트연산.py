# # 비트 연산
# print(7 & 5)
# print(7 | 5)
# # 10진수를 2, 16진수로 변환
# print(bin(10))
# print(hex(10))
# # 2, 16진수 문자열을 10진수로 변환
# print(int('1011',2))
# print(int('b', 16))

# print(0b11011110 & 0b11011)
# print(0x4A3 | 25)
# print(int('0x4A3', 16))
#
# a = bin(0b1011 ^ 0b1101)
# print(a)

# def cod(n):
#     return n ^ KEY
#
# KEY = 1004
# print(cod(1000))
# print(cod(4))
# print(1000 ^ 1004)
# print(4 ^ 1004)
# # 시프트 연산자
# print(bin(0b1101 << 2))
# print(bin(0b1101 >> 2))

# # 시프트 연산자를 이용한 프로그래밍
# for i in range(5):
#     print(bin(1 << i), 0b1 << i)
#
# t = 1
# for i in range(5):
#     print(bin(t), t)
#     t = t << 1

# print(~4) # -5

# 실수 값 정확히 출력해보기
t = 0.1
print(f'{t:.50f}')