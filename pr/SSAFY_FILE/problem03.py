############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def check_user_id(user):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    cnt = 0  # cnt(문자열의 길이)를 0으로 초기화
    for id in user['user_id']:  # user 딕셔너리에서 user_id 키에 해당하는 value 값(id)에 대해
        for char in id:         # value 값(id)의 문자열 하나하나에 대해
            cnt +=1             # cnt를 1씩 더해준다. 즉 문자열의 길이
    if cnt >=4 and cnt<16:      # 문자열의 길이(cnt)가 4<=cnt<16 둘다 만족하면
        return True             # True 반환한다.
    else:                       # 그 이외에는
        return False            # False 반환한다.


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
print(check_user_id(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(check_user_id(user_data2))  # False
#####################################################
