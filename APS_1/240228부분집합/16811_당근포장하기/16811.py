import sys
sys.stdin = open('sample_in.txt')

# def func(t):
#     if t == N:
#         print(path)
#         return
#     for i in range(N):
#         if used[i] == True : continue
#         used[i] = True
#         path.append(C[i])
#         func(t+1)
#         path.pop()
#         used[i] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    # 당근을 나눠서 포장해야한다.
    # 같은 크기의 당근은 같은 상자에
    # 비어 있는 상자는 있으면 안됨
    # 한 상자에 N/2개를 초과하는 당근이 있어서도 안됨
    # 위 조건을 만족하면서도 각 상자에 든 당근의 개수는 최소가 되도록 포장
    s = [] # 소 상자
    m = [] # 중 상자
    l = [] # 대 상자
    C.sort()
    result = 0

    # func(0)
# 상자에 당근을 넣는다. 크기가 같다면 당근을 계속 넣는데
# 상자에 당근이 N/2개를 초과하면 안된다.



    for i in range(N):
        for j in range(i, N):
            s = C[:i]
            m = C[i:j]
            l = C[j:]

            if len(s) == 0 or len(m) == 0 or len(l) == 0:
                continue
            # 값이 같다면 같은 상자에 넣어야 한다.
            if len(s) <= N//2 and len(m) <= N//2 and len(l) <= N//2:

                result = max(len(s), len(m), len(l)) - min(len(s), len(m), len(l))

                print(s)
                print(m)
                print(l)
    print(result)


    # for i in range(N):
    #     s.append(C[i])
    #     if C[i] == C[i + 1]:
    #         s.append(C[i + 1])
    #         if len(s) > N // 2:
    #             break

            # if i < N//2:
            #     s.append(C[i])




        # if C[i] == C[i+1] and len(s) <= N/2:
        #     s.append(C[i+1])
        #
        # if len(m) <= N/2:
        # if len(l) <= N/2:




