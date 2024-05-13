n = int(input())
k = int(input())
candidate = list(map(int, input().split()))
photo = {}
for i in range(k):
    recommend = candidate[i]
    if recommend in photo:
        photo[recommend][0] += 1
    elif len(photo) < n:
        photo[recommend] = [1, i]
    else:
        sorted_photo = list(photo.items())
        sorted_photo.sort(key = lambda x: (x[1][0], x[1][1]))
        tmp = sorted_photo[0]
        photo.pop(tmp[0])
        photo[recommend] = [1, i]
ans = list(photo.items())
ans.sort(key = lambda x: x[0])
for i in range(len(ans)):
    print(ans[i][0], end = " ")