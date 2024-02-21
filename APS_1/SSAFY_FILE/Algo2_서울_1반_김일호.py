# 개구리가 K 번 점프했을 때 개구리가 밟은 연잎의 모든 숫자의 합을 구하시오.
# 연잎의 숫자가 양수인 경우 앞
# 연잎의 숫자가 음수인 경우 뒤
# 뒤로 갔다가 앞으로 가면 뒤 + 앞 만큼 앞으로 이동 연속 두 번 이상 뒤로 가면 마지막 뒤 + 앞
# 연잎 범위를 벗어나면 break
import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, (input().split()))
    arr = list(map(int, input().split()))
    # print(arr)
    total = 0 # 움직임과 밟은 숫자는 다르니까
    bonus = 0
    start = 0
    for i in range(K):  # i는 점프 한 경우
        # print(arr[i])
        total = start + arr[i] + bonus  # 시작점은 0
        if arr[i] > 0:
            total += arr[i]
        if arr[i] < 0:
            total += arr[i]
        print(total)
        print('=======')
            # 연잎을 밟았다. arr[i] 만큼 뛰어서, 근데 값이 -2야.
            # 다시 -2칸 만큼 이동

    #     if arr[i] < 0:
    #         move += 1
    #         num += arr[i]
    #         if arr[i] > 0:
    #             move += 1
    #             num += arr[i-1] + arr[i]
    #
    #     if move == K: # K번 만큼 움직이면 종료.
    #         break
    # print(f'#{tc} {num}')
