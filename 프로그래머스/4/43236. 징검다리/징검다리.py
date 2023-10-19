
def solution(distance, rocks, n):
    ans = 0
    start, end = 0, distance
    rocks.sort()
    rocks.append(distance)
    while start <= end:
        mid = (start + end) // 2
        pre_stone = 0
        remove_stone = 0
        
        for rock in rocks:
            if rock - pre_stone < mid:
                remove_stone += 1 #pre_stone에 현재 rock을 기억하지 않으면 삭제한 것과 같음
            else:
                pre_stone = rock
                
            if remove_stone > n: #n보다 크면 거리를 줄여야함 
                break
        
        if remove_stone > n:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
        
    return ans