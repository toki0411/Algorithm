N = int(input())
def recursion(length, n, N):  #총길이, 가운데 고유문자 길이, N(문자열위치)
    if N < 3:
        print("moo"[N - 1])
        return
    prev = (length - n) // 2  #가운데를 제외한 반
    if N <= prev:
        return recursion(prev, n-1, N)
    if N > prev + n:
        return recursion(prev, n-1, N - prev - n)
    if N - prev == 1:
        print("m")
        return
    else:
        print("o")
        return

length = 3  #moo S(0)
n = 0
while length < N :
    n += 1
    length = 2 * length + n + 3


recursion(length, n+3, N) #total, midlen
