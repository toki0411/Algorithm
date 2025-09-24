def solution(str):
    stack = []
    for s in str:
        if s == '(':
            stack.append('(')
        elif s == ')' and len(stack) != 0:
            stack.pop()
        else:
            return False
    if len(stack): return False
    return True