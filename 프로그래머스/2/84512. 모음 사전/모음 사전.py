from itertools import product
def solution(word):
    voca = []
    answer = 0
    for i in range(1, 6):
        d = list(map("".join, product(['A','E','I','O','U'], repeat=i)))
        voca.extend(d)
    voca.sort()
    for i in range(len(voca)):
        if word == voca[i]:
            answer = i + 1
    return answer