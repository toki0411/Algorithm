n, k = map(int, input().split())
pascal = [[0]]
for depth in range(2, n+2):
    pascal.append([0]*depth)  #맨 위에 꺼 빼고 삼각형 모양 만듬

# pascal[i] = [1, ?, ?, ..., ?, 1]에서 i는 nCk에서 n, 리스트의 인덱스는 k를 의미
# nC0 = 1
pascal[1] = [1, 1] # 0, 1층은 전부 1로만 구성
for depth in range(2, n): #0층부터 n-1층까지
    pascal[depth][0] = 1 #항상 모든 층의 제일 왼쪽은 1
    pascal[depth][-1] = 1 #항상 모든 층의 제일 오른쪽은 1
    for idx in range(1, depth):
        pascal[depth][idx] = (pascal[depth-1][idx] + pascal[depth-1][idx-1]) % 10007
if k == 0 or k == n:
    print(1)
else:
    print((pascal[n-1][k-1] + pascal[n-1][k]) % 10007)
