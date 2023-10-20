def solution(number, k):
    ans = []; limit = len(number) - k
    for num in number:
        while ans and k > 0 and ans[-1] < num:
            ans.pop()
            k-=1
        ans.append(num)
        
    return ''.join(ans[:limit])