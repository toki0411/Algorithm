def binarySearch(target, times):
    start = 0
    end = max(times) * target
    ans =0
    while end >= start:
        mid = (start + end) // 2
        people = 0
        for i in times:
            people += int(mid // i)
            if people >= target: break #성능 최적화
        if people >= target:
            end = mid -1
            ans = mid
        else:
            start = mid + 1
    return ans


def solution(n, times):
    ans = binarySearch(n, times, )
    return ans