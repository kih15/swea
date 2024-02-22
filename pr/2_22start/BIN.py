# 10진수를 2진수로 변환 구현
tar = 149
result = []

while tar != 0:
    result.append(tar % 2)
    tar //= 2

result.reverse()
print(result)