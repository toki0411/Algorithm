import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import deque

def solution(board):
    n = len(board); m = len(board[0])
    rx = ry = 0;
    dist = [[987654321 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                dist[i][j] = 0
                rx = i;
                ry = j
                break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([(rx, ry, 0)])

    while q:
        x, y, c = q.popleft()

        if board[x][y] == 'G':
            return c

        for i in range(4):
            nx = x
            ny = y
            #미끄러짐
            while 0 <= nx + dx[i] < n and 0<= ny + dy[i] < m and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]

            if dist[nx][ny] > c + 1:
                dist[nx][ny] = c + 1
                q.append((nx, ny, c+1))
    return -1