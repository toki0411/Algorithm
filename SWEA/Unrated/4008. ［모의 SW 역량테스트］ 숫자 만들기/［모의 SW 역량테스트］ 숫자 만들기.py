def dfs(operator, num, op_arr):
    global max_val, min_val;
    if sum(operator) == 0:
        val = calculate(num, op_arr)
        if val > max_val: max_val = val
        if val < min_val: min_val = val
        return
    for i in range(4):
        if operator[i] > 0:
            operator[i]-=1
            dfs(operator, num, op_arr+[i])
            operator[i]+=1
def calculate(num, op_arr):
    global data
    val = num[0]
    for i in range(len(op_arr)):
        if op_arr[i] == 0:
            val += num[i+1]
        elif op_arr[i] == 1:
            val -= num[i+1]
        elif op_arr[i] == 2:
            val *= num[i+1]
        elif op_arr[i] == 3:
            val = int(val / num[i+1])
    return val

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    operator = list(map(int, input().split()))
    num = list(map(int, input().split()))
    data = ['+', '-', '*', '/']
    max_val = -1e9; min_val = 1e9;    op_arr = []
    dfs(operator, num, op_arr)
    print('#{} {}'.format(tc, max_val-min_val))