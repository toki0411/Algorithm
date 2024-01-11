def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    else:
        k = s // n
        for i in range(n):
            answer.append(k)

        s = s%n
        if s != 0:
            for a in range(len(answer)):
                answer[a] += 1
                s -= 1
                if s == 0:
                    break

        answer.sort()
    return answer

print(solution(2, 9))




