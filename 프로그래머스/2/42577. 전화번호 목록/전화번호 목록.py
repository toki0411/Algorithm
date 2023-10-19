def solution(phone_book):
    answer = True
    phone_book.sort(key = len)
    dict = {}
    for i in phone_book:
        dict[i] = 0
    for i in phone_book:
        for j in range(1, len(i)+1):
            tmp = i[:j]
            if tmp == i:continue
            if tmp in dict.keys():
                answer = False; break;
        if not answer:
            break

    return answer