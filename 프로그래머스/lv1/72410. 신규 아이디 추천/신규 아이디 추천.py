def solution(new_id):
    #1단계
    s = new_id.lower()
    #2단계
    arr2 = []
    for i in s:
        if i.isdigit() or i.islower() or i=='-' or i == '_' or i =='.':
            arr2.append(i)
    #3단계
    arr3 = []
    for i in range(len(arr2)-1):
        if arr3 and arr3[-1] == arr2[i] == '.':
            continue
        else:
            arr3.append(arr2[i])
    arr3.append(arr2[-1])

    #4단계
    if arr3 and arr3[0] == '.':
        arr3.remove('.')
    if arr3 and arr3[-1] == '.':
        arr3.pop()

    #5단계
    if len(arr3) == 0:
        arr3.append('a')

    #6단계
    if len(arr3) >= 16:
        arr3 = arr3[:15]

    if arr3[-1] == '.':
        arr3.pop()

    #7단계
    tmp = arr3[-1]
    while len(arr3) < 3:
        arr3.append(tmp)
    return ''.join(arr3)