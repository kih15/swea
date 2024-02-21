############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def check_email(user):
    pass
    

    # 여기에 코드를 작성하여 함수를 완성합니다.
    lst = [] # 빈 리스트 형성
    for char in user['email']: # user 딕셔너리에서 email 키 값에 해당하는 value 값의 문자열(char) 하나하나에 대해
        lst.append(char)    # lst에 문자열(char)을 하나씩 추가한다.
    if '@' in lst:      # 만약 @가 lst 안에 있다면
        return True     # True 반환
    else:               # 그 이외에는
        return False    # False 반환
                



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'chibbo24@mail.com',
}
print(check_email(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_email(user_data2))  # False
#####################################################
