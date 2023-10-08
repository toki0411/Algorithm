def collatz(num, cnt):
    if num == 1:
        return cnt
    if cnt >= 500:
        return -1
    elif num % 2 == 0:
        num = int(num // 2)
        return collatz(num, cnt + 1)
    elif num % 2 == 1:
        num = num * 3 + 1
        return collatz(num, cnt + 1)
def solution(num):
    return collatz(num , 0)