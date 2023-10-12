def solution(numbers):
    num = []
    for i in numbers:
        num.append(str(i))
    num.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(num)))