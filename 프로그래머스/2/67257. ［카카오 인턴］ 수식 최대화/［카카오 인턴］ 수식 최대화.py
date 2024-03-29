from itertools import permutations
import re
def solution(expression):
    expression = re.split('([*+-])', expression)
    operators = list(permutations(['-','*','+']))
    results = []
    
    for operator in operators:
        exp = expression.copy()
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1] + exp[idx] + exp[idx+1]))
                del exp[idx:idx+2]   
        results.append(abs(int(exp[0])))
   
    return max(results)
