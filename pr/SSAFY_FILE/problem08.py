############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def find_solo(number_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    lst = []    # 빈 리스트 형성
    s = list(set(number_list)) # number_list에서 중복 요소가 제거된 리스트 형성

    for num in s:   # 중복 요소가 제거된 리스트 내의 숫자에 대해 
        cnt = 0 # cnt 0으로 초기화
        for num_count in number_list:   # number_list의 숫자에 대해
            if num == num_count:    # s는 중복 요소 제거. 대표 숫자를 number_list와 비교해서 개수를 count해준다.
                cnt+=1 # cnt에 1을 더해준다.
        lst.append(cnt) # 숫자가 몇 개 있는지 나타내느 cnt를 lst에 추가한다.
    
    return s[lst.index(1)]  # s와 lst의 길이는 같고 lst에 1이 있는 인덱스(짝이 맞지 않은)를 찾아 s의 값 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################
