############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    pass



    # 여기에 코드를 작성하여 함수를 완성합니다.
    (x,y)= current # x와 y에 current의 첫번째, 두번째 좌표 반환
    if M == 0:  # M이 0이면 y-1
        y-=1
    elif M == 1:  # M이 1이면 y+1
        y+=1
    elif M == 2:  # M이 2이면 x-1    
        x-=1
    elif M == 3:  # M이 3이면 x+1
        x+=1
    if x>=0 and x<=N and y>=0 and y<=N: # 이동한 좌표가 (0,0)에서 (N,N) 사이에 있으면
        return True # True 반환
    else:   # 그 이외에는 
        return False # False 반환
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
