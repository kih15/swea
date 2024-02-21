N = int(input())

hap = 0
for x in range(N):
    sum1 = x
    for i in str(x):
        sum1 += int(i)
    if sum1 == N:
        hap = x
        break
print(hap)