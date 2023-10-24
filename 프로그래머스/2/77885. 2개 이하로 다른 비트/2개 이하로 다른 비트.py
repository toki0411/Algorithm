def f(x):
    if x % 2 == 0:
        return x + 1
    else:
        x = '0'+bin(x)[2:]
        for i in range(len(x) - 1, -1, -1):
            if x[i] == '0':
                ans = list(x)
                ans[i] = '1';
                ans[i + 1] = '0'
                return int(''.join(ans), 2)
def solution(numbers):
    return [f(number) for number in numbers]