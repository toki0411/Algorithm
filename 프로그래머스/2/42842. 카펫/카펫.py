def solution(brown, yellow):
    for i in range(3, 2500):  #가로
        for j in range(i+1):  #세로
            if i * j == brown + yellow :
                if i* j - 2 * i - 2 * j + 4 == yellow:
                    return [i, j]