n, k = map(int, input().split())
arr = list(map(int, input().split()))
use = [];
cnt = 0
if n >= k:
    print(0)
    exit()
for i in range(k):
    if arr[i] in use:
        continue
    if len(use) < n:
        use.append(arr[i])
    else:
        tmp_arr = arr[i + 1:];
        far_one = 0; temp = 0
        for j in range(len(use)):
            if use[j] not in tmp_arr:
                temp = j
                break
            else:
                idx = tmp_arr.index(use[j])
                if idx > far_one:
                    far_one = idx
                    temp = j
        use[temp] = arr[i]
        cnt += 1

print(cnt)
