import re
def solution(id_list, report, k):
    id = {}
    for i in id_list:
        id[i] = 0
    report_dict = {}
    for i in report:
        reporter, reported = i.split() #신고자, 신고 당한 사람 
        if reported not in report_dict.keys():
            report_dict[reported] = [reporter]
        else:
            if reporter not in report_dict[reported]:         
                report_dict[reported].append(reporter)

    for i in report_dict:
        
        if len(report_dict[i]) >= k:
            for j in report_dict[i]:
                id[j] += 1

    
    return list(id.values())