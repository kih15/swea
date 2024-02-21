'''
10
-7 -5 2 3 8 -2 4 6 9
'''
def f(arr, N):
    for i in range(1 << N): # 1<<n : 부분 집합의 개수
        s = 0
        for j in range(N): # 원소의 수만큼 비트를 비교함
            if i & (1 << j): # i의 j번 비트가 1인 경우
                s += arr[j]
                # print(arr[j], end = ' ') # j번 원소 출력
        # print(s)
        if s == 0:
            return True
    return False

N = int(input())
arr = list(map(int, input().split()))
print(f(arr, N))