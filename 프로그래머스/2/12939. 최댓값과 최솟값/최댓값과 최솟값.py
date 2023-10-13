def solution(s):
    arr = list(map(int, s.split(' ')))
    
    ans = []
    
    ans.append(str(min(arr)));ans.append(' ');
    ans.append(str(max(arr)));
    return ''.join(ans)
               
    