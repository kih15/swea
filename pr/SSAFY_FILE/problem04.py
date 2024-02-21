############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def compare_pw(user):
    pass

    # 여기에 코드를 작성하여 함수를 완성합니다.
    cnt =0  # cnt(문자열의 길이) 0으로 초기화
    for pw in user['password']: # user 딕셔너리에서 password 키 값에 해당하는 value 값(pw)에 대해
        for char in pw:         # value 값(pw)의 문자열(char) 하나하나에 대해
            cnt +=1             # cnt를 1씩 더해준다. 즉 문자열의 길이
    if cnt>=8 and cnt <32 and user['password'] == user['password_confirm']: # cnt(문자열의 길이)가 8<=cnt<32 라는 조건1과 user 딕셔너리에서 password 키 값에 해당하는 value 값과 password-confirm 키 값에 해당하는 value 값이 일치한다는 조건2를 만족하면 
        return True # True 반환
    else:           # 그 이외에는
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
    'email': 'goodjob24@mail.com',
}
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################
