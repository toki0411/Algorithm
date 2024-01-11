import heapq
import sys

input = sys.stdin.readline
n = int(input())

leftheap = []  #최대힙
rightheap = []  #최소힙

for i in range(n):
    num = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -num)
    else:
        heapq.heappush(rightheap, num)

    if len(leftheap) > 0 and len(rightheap) > 0 and -1 * leftheap[0] > rightheap[0]:
        left = heapq.heappop(leftheap)
        right = heapq.heappop(rightheap)

        heapq.heappush(leftheap, -1 * right)
        heapq.heappush(rightheap, left * -1)

    print(leftheap[0] * -1)
