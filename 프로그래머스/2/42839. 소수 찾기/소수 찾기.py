import itertools
def prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num // 2)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    num = list(numbers);
    prime = []; val = []

    for i in num:
        val.append(int(i))

    for i in range(2, len(num)+1):
        a = list(itertools.permutations(num, i))
        for j in range(len(a)):
            temp = []
            for l in range(i):
                temp.append(a[j][l])
            val.append(int(''.join(temp)))

    arr = list(set(val))
    for i in arr:
        if prime_number(i)==True:
            prime.append(i)
    return len(prime)