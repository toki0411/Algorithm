import re
def division(n, q):
    ans = []
    while n > 0:
        n, mod = divmod(n, q)
        ans.append(str(mod))
    ans = ans[::-1]
    return ''.join(ans)
def is_prime(n):
    if n<2: return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
def solution(n, k):
    ans = 0
    str = division(n, k)
    pArr = re.split('0', str)
    while '' in pArr:
        pArr.remove('')

    for p in pArr:
        if is_prime(int(p)):
            ans+=1
    return ans