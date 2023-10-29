def solution(board, skill):
    ans = update(board, skill)
    return ans
def update(board, skill):
    diff = [[0] * (len(board[0])+1) for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        d = -degree if type == 1 else degree
        diff[r1][c1] += d
        diff[r1][c2+1] += -d
        diff[r2 + 1][c1] += -d
        diff[r2+1][c2+1] += d
    for r in range(len(board)):
        for c in range(1, len(board[0])):
            diff[r][c] += diff[r][c-1]
    for c in range(len(board[0])):
        for r in range(1, len(board)):
            diff[r][c] += diff[r-1][c]
    #board를 돌면서 누적합을 더해줌
    cnt = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += diff[r][c]
            if board[r][c] > 0:
                cnt += 1
    return cnt