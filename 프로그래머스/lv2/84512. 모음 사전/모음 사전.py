import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 자기 호출 개수 제한

def dictionary(num, cnt, goal):
    if num == goal:
        return cnt
    if num % 10 > 0 and num % 10 < 5:
        return dictionary(num + 1, cnt+1, goal)
    elif num % 10 == 5:
        if num % 10000 == 5555:
            return dictionary(num + 4445, cnt + 1, goal)
        elif num % 1000 == 555:
            return dictionary(num + 445, cnt + 1, goal)
        elif num % 100 == 55:
            return dictionary(num + 45, cnt + 1, goal)
        else:
            return dictionary(num + 5, cnt+1, goal)
    s = str(num)

    if s.count('0') == 4:
        return dictionary(num + 1000, cnt+1, goal)
    elif s.count('0') == 3:
        return dictionary(num + 100, cnt+1, goal)
    elif s.count('0') == 2:
        return dictionary(num + 10, cnt+1, goal)
    elif s.count('0') == 1:
        return dictionary(num + 1, cnt+1, goal)

def solution(word):
    arr2 = []
    for i in word:
        if i =='A':
            arr2.append(str(1))
        elif i == 'E':
            arr2.append(str(2))
        elif i == 'I':
            arr2.append(str(3))
        elif i == 'O':
            arr2.append(str(4))
        elif i == 'U':
            arr2.append(str(5))
    while len(arr2) < 5:
        arr2.append(str(0))
    ans = dictionary(10000, 1, int(''.join(arr2)))
    return ans