import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    back = 0
    # 연잎의 숫자가 양수이면 앞으로 음수이면 뒤로 점프
    # 점프 횟수 카운팅
    # 뒤로 간 경우 앞으로가면 직전에 뒤로 간 칸 만큼 더 앞으로 점프
    # 연잎 범위에서 벗어나면 점프 X
    jump = 0
    jump += A[0]  # A[0] 만큼 점프
    cnt += A[jump]  # 점프한 곳의 값을 cnt에 저장
    for i in range(K-1):
        if A[jump] < 0:
            back = A[jump]
            jump += A[jump]
            if jump < 0 or jump > len(A):
                break
            cnt += A[jump]
        else: # cnt의 값이 양수인 경우
            jump += A[jump] - back
            back = 0
            if jump < 0 or jump > len(A):
                break
            cnt += A[jump]

        # A[0] 을 뛴다. 뛰었을 때 연잎을 밟아서 그 값을 cnt 에 더해준다.
    # jump = 0
    # cnt = 0
    # back = 0
    # jump += A[0]
    # cnt += A[jump]
    # # 연잎의 값 만큼 뛴다. 그 값이 음수라면 뒤로 뛰고 back 에 저장해준다. 그 값을 cnt에 더해준다.
    # for i in range(K-1):
    #     if A[jump] < 0:
    #         back = A[jump]
    #         jump += A[jump]
    #         if jump < 0 or jump >= len(A):
    #             break
    #         cnt += A[jump]
    #
    #     # 양수라면 back에 저장된 값 + 연잎의 값만큼 뛴다. 밟은 연잎의 값만큼 cnt 에 더해준다.
    #     else:
    #         jump += A[jump] - back
    #         back = 0
    #         if jump < 0 or jump >= len(A):
    #             break
    #         cnt += A[jump]
        # 음수라면 뒤로 뛰고 back에 다시 저장
        # K번만큼 반복
        # 연잎의 범위를 벗어나면 break
    print(cnt)


