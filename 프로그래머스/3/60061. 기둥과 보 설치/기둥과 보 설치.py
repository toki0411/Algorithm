def possible(result):
    for x, y, kind in result:
        if kind == 0:        #기둥
            #바닥 위에 있거나 
            if y == 0 : continue
            #보의 한쪽 끝 부분 위에 있거나
            elif (x-1,y,1) in result or (x,y,1) in result:
                continue
            #다른 기둥 위
            elif (x,y-1,0) in result:
                continue
            else:
                return False
        else:                #보
            #한쪽 끝 부분이 기둥 위에 있거나
            if (x,y-1,0) in result or (x+1,y-1,0) in result : continue
            #양쪽 끝 부분이 다른 보와 동시에 연결
            elif (x-1,y,1) in result and (x+1,y,1) in result : continue
            else:
                return False
    return True  
    
def solution(n, build_frame):
    result = set()
    
    for x, y, a, cmd in build_frame:
        item = (x,y,a)
        if cmd == 0: #삭제
            result.remove(item)
            if possible(result) == False:
                result.add(item)
        elif cmd == 1: #설치
            result.add(item)
            if possible(result) == False:
                result.remove(item)
    answer = map(list, result)
    return sorted(answer, key = lambda x: (x[0], x[1], x[2]))