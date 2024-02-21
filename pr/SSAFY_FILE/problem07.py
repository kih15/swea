############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def tidy_up_company(email_list):
    ans = {}    # 빈 딕셔너리 형성
    set_email_list = list(set(email_list))  # email_list에서 set으로 중복 요소 제거 후 list 로 반환
    for name in set_email_list:     # set_email_list의 항목에 대해
        cnt = 0 # cnt 0으로 초기화
        for name_count in email_list:   # 입력받은 email_list의 항목에 대해
            if name == name_count: # set_email_list는 중복요소가 제거된 리스트. 기업 이름이 1개씩 있으므로 email_list와 이름이 같다면 count해준다.
                cnt+=1  # cnt에 1을 더해준다.
                ans[name] = cnt # ans라는 빈 딕셔너리에 name 키값과 cnt value값 추가
    return ans # 최종 딕셔너리 반환
        

    # 여기에 코드를 작성하여 함수를 완성합니다.
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))
# {'Koogle': 6, 'JCloud': 2, 'GaKao': 6, 'School': 3, 'Maver': 3}
#####################################################
