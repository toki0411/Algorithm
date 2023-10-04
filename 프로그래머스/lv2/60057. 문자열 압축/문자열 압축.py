def cutStr(s, k):
    ans = []
    for i in range(0,len(s),k):
        temp = []
        for j in range(k):
            if i + j >= len(s):
                break;
            temp.append(s[i+j])
        str = "".join(temp)
        ans.append(str)
    return ans
def solution(s):
    limit = int(len(s) / 2); min_len = len(s)
    for i in range(limit, 0, -1):  #한 덩이 셋팅
        temp = cutStr(s, i); ans = []
        dic = {}
        for j in range(1, len(temp)):
            if temp[j-1] == temp[j]:
                if temp[j-1] in dic:
                    dic[temp[j-1]] += 1
                else :
                    dic[temp[j-1]] = 2  #있으면 +1 없으면 만들어줌
            else :
                ans.append(temp[j - 1])
                if len(dic) != 0:
                    ans.append(str(dic[temp[j - 1]]))
                    del dic[temp[j-1]]

        ans.append(temp[len(temp)-1])
        if len(dic)!=0:
            ans.append(str(list(dic.values())[0]))
        sum = 0
        for l in ans:
            sum += len(l)
        min_len = min(sum, min_len)

    return min_len

