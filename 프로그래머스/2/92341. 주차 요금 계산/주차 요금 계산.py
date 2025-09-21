from math import ceil
def solution(fees, records):
    dict = {}
    answer = []
    for record in records:
        rec = record.split(' ')
        if rec[1] in dict:
            dict[rec[1]].append([rec[0], rec[2]])
        else:
            dict[rec[1]] = []
            dict[rec[1]].append([rec[0], rec[2]])
    for i in dict:
        if len(dict[i]) % 2 != 0 :
            dict[i].append(['23:59', 'OUT'])
        time = 0
        for j in range(0, len(dict[i]), 2):
            in_time = dict[i][j][0].split(':')
            out_time = dict[i][j + 1][0].split(':')
            in_time = int(in_time[0]) * 60 + int(in_time[1])
            out_time = int(out_time[0]) * 60 + int(out_time[1])
            time += abs(out_time - in_time)
        if time <= fees[0]:
            answer.append([fees[1], i])
        else:
            answer.append([fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3], i])
    answer.sort(key = lambda x:x[1])
    ans = []
    for i in range(len(answer)):
        ans.append(answer[i][0])
    return ans
