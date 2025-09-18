import sys
input = sys.stdin.readline
N = int(input())
s = 0
for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'add':
        s |= (1 << int(cmd[1]))
    elif cmd[0] == 'remove':
        s &= ~(1 << int(cmd[1]))
    elif cmd[0] == 'check':
        if s & (1 << int(cmd[1])):
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        s ^= (1 << int(cmd[1]))
    elif cmd[0] == 'empty':
        s = 0
    elif cmd[0] == 'all':
        s = (1<<21) - 1
