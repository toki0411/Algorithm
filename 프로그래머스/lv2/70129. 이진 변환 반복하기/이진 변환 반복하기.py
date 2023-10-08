def divideNumber(num):  #2진법으로 변환
    if num == 1:
        return True
    else:
        div = num; ans = []
        while div != 0:
            div, mod = div // 2, div % 2
            ans.append(str(mod))
    return ''.join(ans[::-1])

def solution(s):
    cnt = 0; zero = 0;answer= []
    while True:
        arr = []
        for i in s:
            if i!='0':
                arr.append(i)
            else:
                zero +=1
        s = divideNumber(len(arr));  cnt += 1
        if s == True:
            break

    answer.append(cnt); answer.append(zero)
    return answer