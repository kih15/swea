N = int(input())
for i in range(N-1, N):
    print(' '*i + '*')
for i in range(1, N):
    print(' '*(N-i-1) + '* '*(i+1))