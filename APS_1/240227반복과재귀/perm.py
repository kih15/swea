# 중복 순열
def perm1(i, r):     # i: 뽑는 순번, r: 뽑으려는 총 개수

    if i >= r:      # 뽑는 순번이 총 개수와 같거나 커지면 더 이상 뽑지 않도록 base case 설정
        print(*choice)
        return

    else:
        for j in range(len(card)):
            choice[i] = card[j]     # append
            perm1(i+1, r)
            choice[i] = 0           # pop

# 순열
def perm2(i, r):
    if i >= r:      # 뽑는 순번이 총 개수와 같거나 커지면 더 이상 뽑지 않도록 base case 설정
        print(*choice)
        return

    else:
        for j in range(len(card)):
            if used[j] == 0:    # 만약 카드가 사용되지 않았다면
                used[j] = 1     # 사용 처리
                choice[i] = card[j]     # append # 선택 카드에 추가
                perm2(i+1, r)
                choice[i] = 0           # pop
                used[j] = 0

# 원본 변경 순열
def perm3(i, r):
    if i >= r:
        print(*card[:r])
        return
    else:
        for j in range(i, len(card)):
            card[i], card[j] = card[j], card[i]
            perm3(i+1, r)
            card[i], card[j] = card[j], card[i]



# card = ['A', 'B', 'C']
card = ['A', 'B', 'C', 'D', 'E']

# r = 2
r = 3

choice = [0] * r # r: 뽑으려는 개수

perm1(0, r)
print('---')
used = [0] * len(card)  # 해당 카드가 중복 사용되지 않도록
perm2(0,r)
print('---')
perm3(0, r)