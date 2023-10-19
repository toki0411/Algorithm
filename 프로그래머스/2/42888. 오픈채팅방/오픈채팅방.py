def solution(record):
    dict = {};answer = []
    for i in record:
        arr = i.split()
        if arr[0]=='Enter':
            dict[arr[1]] = arr[2]
        elif arr[0] == 'Change':
            dict[arr[1]] = arr[2]
    for i in record:
        arr = i.split(); tmp = []
        if arr[0] == "Enter":
            tmp.append(dict[arr[1]])
            tmp.append("님이 들어왔습니다.")
            
        elif arr[0]=="Leave": 
            tmp.append(dict[arr[1]])
            tmp.append("님이 나갔습니다.")
        else: continue    
        answer.append(''.join(tmp))
    
    return answer