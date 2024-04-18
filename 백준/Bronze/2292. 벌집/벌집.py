import sys
sys.stdin.readline
N = int(input())
MAX = 1000000000
if N == 1:
    print(1)
    exit()
d = 5
room = 2
idx = 2
while True:
    if idx <= N <= idx + d:
        print(room)
        break
    if idx > MAX: break
    room += 1
    idx += (d+1)
    d += 6