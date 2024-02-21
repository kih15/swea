# print(ord('0'))
# print(ord('1'))
# print(ord('9') - ord('0'))

def itoa(a):
    s = ''
    while a > 0:
        s = chr(a % 10 + ord('0')) + s
        a //= 10
    return s
ans = itoa(123)
print(ans)