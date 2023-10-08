n = int(input())
s = str(n); key1 = False; key2 = False
arr = []
for i in s:
    if i == '0':
        key1 = True
    arr.append(int(i))
if n % 3 == 0:
    key2 = True

if key1 and key2:
    arr = sorted(arr, reverse=True)
    for i in arr:
        print(i, end='')

else :
    print(-1)