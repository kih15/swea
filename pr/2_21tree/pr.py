def inorder(t):
    global answer
    # t번 노드가 존재하는가?
    if t:
        # 왼쪽 자식 노드 : L
        inorder(cleft[t])
        # 부모 노드 : V
        # t번 노드에서 처리할 일을 코드로 작성
        # t번 노드에 적혀있는 알파벳을 정답 문자열에 이어 붙이기
        answer += node[t]

        # 오른쪽 자식 노드 : R
        inorder(cright[t])


T = 10

for tc in range(1, T + 1):
    # 정점(노드)의 수
    N = int(input())

    # 왼쪽 자식 번호 저장
    cleft = [0] * (N + 1)
    # 오른쪽 자식 번호 저장
    cright = [0] * (N + 1)

    # 노드 번호를 알파벳으로 식별 할수 있도록 저장
    node = [0] * (N + 1)

    # 트리 만들기
    for i in range(N):
        # 노드의 정보를 한줄씩 읽어오기
        info = input().split()
        # 쪼개서 가져온 다음에 글자의 개수 세보기
        # 0 번째 => 노드 번호
        # 1 번째 => 알파벳
        # 2 번째 => 왼쪽 자식 번호
        # 3 번째 => 오른쪽 자식 번호

        # 노드 번호
        p = int(info[0])
        # 입력 받은 길이 측정
        l = len(info)

        if l >= 3:
            cleft[p] = int(info[2])
            if l == 4:
                cright[p] = int(info[3])

        # p번 노드의 알파벳은?
        node[p] = info[1]

    answer = ""
    # 1번 노드부터 방문 시작
    inorder(1)
    print(f"#{tc} {answer}")