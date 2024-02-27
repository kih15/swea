def counting():
    for l in range(3):
        if perm[l] == perm[l + 1] == perm[l + 2] : return True
        return False

def perm1(i, r):
    global cnt
    if i == r:
        if counting(): cnt += 1
        return
    for j in range(len(card)):
        perm[i] = card[j]
        perm1(i+1, r)
        perm[i] = 0



card = ['A', 'J', 'Q', 'K']
r = 5
perm = [0] * r
cnt = 0
perm1(0, r)
print(cnt)
