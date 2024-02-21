############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len, sum 함수를 사용하지 않습니다.
def average_cost(cost_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_cost = 0    # 전체 cost의 합을 0으로 초기화
    len_cost = 0    # cost 개수를 0으로 초기화
    for cost in cost_list:  # cost_list 안의 cost에 대해서
        sum_cost += cost    # cost는 sum_cost에 더해준다
        len_cost +=1        # cost 개수는 1씩 더해준다

    return (sum_cost/len_cost)  # 평균 = 요소의 총합/요소의 개수




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_cost([25, 40, 50, 55]))  # 42.5
print(average_cost([60, 70, 90, 80, 100, 35])) # 72.5
#####################################################
