K = 3
N = 6
arr = [0, 1, 0, 1, 1, 1]
ans = 0
cnt = 0
for i in range(N):
    if arr[i] == 0:
        if cnt == K:
            ans += 1
        cnt = 0
    else:   # arr[i] ==1
        cnt += 1
        if i == N-1 and cnt == K:
            ans += 1

print(ans)


    # if arr[i]: # 0만 구분해도 되면 이렇게 가능
    #     cnt += 1
    # elif arr[i] == 0 or i == N - 1:
