N = int(input())
for i in range(N-1, N):
    print(' '*i + '*')
for i in range(1, N-1):
    print(' '*(N-i-1) + '*' + ' '*(2*i-1) + '*')
for i in range(N-1, N):
    if N == 1:
        break
    print('*'*(2*N-1))