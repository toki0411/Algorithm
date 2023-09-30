def solution(my_string, indices):
    indices = sorted(indices)
    arr = []; k=0
    for i in range(len(my_string)):
        if k <= len(indices) - 1 and indices[k] == i :
            k+=1
            continue;
        else:
            arr.append(my_string[i])
    answer = "".join(arr)
    return answer