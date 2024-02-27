def p(num,n):
    if num==n:
        for i in range(n):
            print(arr[select[i]], end=' ')
        print()
    else:
        for j in range(num,n):
            select[num],select[j] = select[j],select[num]
            p(num+1,n)
            select[num],select[j] = select[j],select[num]

n=6
arr = [9,5,5,1,4,2]
select = [i for i in range(n)]
p(0,n)