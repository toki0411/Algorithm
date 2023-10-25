from math import ceil


def solution(fees, records):
    dict = {}; answer = [];

    for i in records:
        tmp = i.split(' ')
        if tmp[1] in dict:
            dict[tmp[1]].append([tmp[0],tmp[2]])
        else:
            dict[tmp[1]] = []
            dict[tmp[1]].append([tmp[0], tmp[2]])
    for i in dict:
        if len(dict[i]) %2 !=0:
            dict[i].append(['23:59', 'OUT'])
        time = 0
        for j in range(0,len(dict[i]),2):
            in_time = dict[i][j][0].split(':')
            out_time = dict[i][j+1][0].split(':')
            in_time = int(in_time[0])*60 + int(in_time[1])
            out_time = int(out_time[0])*60 + int(out_time[1])
            time += abs(out_time-in_time)
        # 주차요금 계산
        if time < fees[0]:
            answer.append([fees[1], i])
        else:
            answer.append([fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3], i])
    answer.sort(key = lambda x:x[1])


    return [i[0] for i in answer]