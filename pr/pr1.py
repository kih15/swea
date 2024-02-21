for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
num = 456789
c = [0] * 12
for i in range(6):
    c[num % 10] += 1
    num //= 10
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue # triplete이 한번 더 있는 경우 찾아내기 위함.
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1       # c를 12칸 만들어 주는 이유: 메모리를 더 쓰더라도 수식을 간단하게 만들기 위해서
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2: print("Baby Gin")
else: print("Lose")