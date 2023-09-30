def solution(arr1, arr2):
    answer = []; limit = len(arr2[0])
    for i in arr1:
        temp = []
        for j in range(limit):
            second = []
            for k in arr2:
                second.append(k[j])
            sum = 0
            for r in range(len(i)):
                sum += i[r] * second[r]
            temp.append(sum)
        answer.append(temp)
    return answer