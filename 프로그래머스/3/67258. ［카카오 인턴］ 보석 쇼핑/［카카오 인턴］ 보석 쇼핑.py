def solution(gems):
    start, end = 0, 0
    kind = len(set(gems))
    ans = [0, len(gems)-1]
    dict = {gems[0]:1}  # 시작위치의 보석
    while end < len(gems):
        if len(dict) < kind:  # 현재 가진 보석의 종류가 전체 종류를 채우지 못했다면
            end += 1  # 끝 포인터를 한 칸 오른쪽으로 옮기고 
            if end == len(gems):
                break
            dict[gems[end]] = dict.get(gems[end], 0) + 1  # 보석을 추가함
        else:
            if (end - start + 1) < (ans[1]-ans[0]+1) : ans = [start, end]  # 현재 저장된 ans 값과 비교하여 더 작은 쪽을 선택 
            
            if dict[gems[start]] == 1:
                del dict[gems[start]]
            else:
                dict[gems[start]] -=1
            start +=1  # 탐색이 끝났다면 start를 한 칸 이동해 새로운 탐색 시작 
    # 저장된 ans의 구간은 배열 값이라 +1 해줘야 함 
    ans[0] +=1
    ans[1] +=1
            
    return ans