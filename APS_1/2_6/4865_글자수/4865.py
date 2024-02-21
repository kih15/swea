import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    count = 0
    max_cnt = 0
    for i in range(len(str1)):
        # print(str1[i])
        for j in range(len(str2)):
            # print(str2[j])
            if str1[i] == str2[j]:
                count += 1
        print(count)
    # if max_cnt < count:
    #     max_cnt = count
    # print(max_cnt)