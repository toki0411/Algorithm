N = int(input())
garo, sero = map(int, input().split())
dot = set()
list = []
cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    dot.add((x,y))
    list.append([x,y])
for i in list:
   x = i[0]; y = i[1]
   cx = x; cy = y + sero
   if (cx, cy) not in dot:
       continue
   bx = x + garo; by = y
   if (bx, by) not in dot:
       continue
   dx = x + garo; dy = y + sero
   if (dx, dy) not in dot:
       continue
   cnt += 1
print(cnt)