import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    test_case, N = input().split()
    arr = input().split()
    number_list = ["ZRO", "ONE", "TWO", "THR", 'FOR', "FIV", "SIX", "SVN", "EGT", "NIN"]

    print(test_case)
    for number in number_list:
        for i in range(int(N)):
            if number == arr[i]:
                print(number, end=' ')