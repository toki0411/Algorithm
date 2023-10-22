def divide(str):
    u = []; v = []
    left = 0; right = 0
    for i in range(len(str)):
        if str[i] =='(':
            left += 1
        if str[i] == ')':
            right +=1
        if left == right:
            u = str[:i+1]
            if i+1 < len(str):
                v = str[i+1:]
            break
    
    return [''.join(u),''.join(v)]
def check(str):
    #str 이 올바른 문자열인지 체크 
    stack = []
    for i in str:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return False if len(stack) else True
def rec(p):
    result = []
    if not len(p):return ""
    str_arr = divide(p); u = str_arr[0]; v = str_arr[1]
    if check(u) : #u가 올바른 괄호 문자열 이라면 
        result.append(u)
        result.append(rec(v))
    else:  #u가 올바른 괄호 문자열이 아니라면 
        tmp = ['(']
        tmp.append(rec(v))
        tmp.append(')')
        u = u[1:-1]
        for c in u:
            if c == '(':
                tmp.append(')')
            else:
                tmp.append('(')
        result.append(''.join(tmp))
    return ''.join(result)
def solution(p):
    answer = rec(p)
            
    #재귀 모듈화 
    return answer