k = int(input())

def recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n % 2 == 0:
        return recursion(n//2)
    else:
        return recursion(1 - recursion(n//2) )
print(recursion(k - 1))
