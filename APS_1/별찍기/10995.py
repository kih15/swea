N = int(input())
for j in range(N):
    for i in range(N-1, N):
        if j % 2 == 0:
            print('* '*(i+1))
        else:
            print(' *'*(i+1))