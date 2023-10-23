def checkDistance(left, right, v):
    mid_arr = [2,5,8,0]
    idx_x = mid_arr.index(v); idx_y = 1
    left_distance = abs(left[0]-idx_x) + abs(left[1]-idx_y)
    right_distance = abs(right[0]-idx_x) + abs(right[1]-idx_y)
    return left_distance, right_distance, idx_x

def solution(numbers, hand):
    ans = []; left = [3, 0]; right = [3, 2]; left_arr = [1,4,7]; right_arr = [3,6,9]; 
    for i in numbers:
        if i in [1,4,7]: # 왼손 담당
            left = [left_arr.index(i), 0]
            ans.append('L')
        elif i in [3,6,9]: # 오른손 담당
            right = [right_arr.index(i), 2]
            ans.append('R')
        else:
            l, r, idx = checkDistance(left, right, i)
            if l == r:
                if hand == 'left':
                    left = [idx, 1]
                    ans.append('L')
                else:
                    right = [idx, 1]
                    ans.append('R')      
            elif l < r: #왼손 사용 
                left = [idx, 1]
                ans.append('L')
            else: # 오른손 사용 
                right = [idx, 1]
                ans.append('R')
    
    return ''.join(ans)