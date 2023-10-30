def solution(triangle):
    n = len(triangle)
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                val = triangle[i-1][j]
            elif j == len(triangle[i])-1:
                val = triangle[i-1][j-1]
            else:
                val = max(triangle[i-1][j-1],triangle[i-1][j])
            triangle[i][j]+=val
    return max(triangle[n-1])