def solution(s, n):
    arr = []
    for i in s:
        if i == ' ':
            arr.append(' ')
        else:
            num = ord(i);
            num += n
            if num > 90 and ord(i) < 91:
                num -= 26
            elif num > 122 and ord(i) < 123:
                num -= 26
            arr.append(chr(num))
    answer = "".join(arr)
    return answer