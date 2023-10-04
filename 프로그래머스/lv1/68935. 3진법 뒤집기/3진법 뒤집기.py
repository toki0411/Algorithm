def radixChange(num , radix):
    nums = []
    while num:
        num , div = divmod(num, radix)
        nums.append(str(div))
    return ''.join(nums)
def solution(n):
    new = str(radixChange(n, 3))
    answer = 0;

    idx = len(new)-1
    for i in range(len(new)):
        a = (pow(3,idx) * int(new[i]))
        idx -=1
        answer += a

    return answer