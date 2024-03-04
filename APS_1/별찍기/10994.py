N = int(input())
for i in range(N-1, N):
    print('*'*(4*i+1))
for i in range(N):
    print('* '*(2*i+1))
for i in range(N-1, N):
    print('*'*(4*i+1))
    # 1일때 1
    # 2일때 5
    # 3일때 9
    # 4일때 13