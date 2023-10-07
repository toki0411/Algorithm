def solution(s):
    arr = list(s); idx = 0;
    for i in range(len(arr)):
        if arr[i] == ' ':
            idx = 0; continue
        elif idx % 2 == 0:
            arr[i] = arr[i].upper()
        else:
            arr[i] = arr[i].lower()
        idx +=1
    answer = "".join(arr)
    return answer