s = input()
arr = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        str = s[i:j]
        arr.append(str)
result = list(set(arr))
print(len(result))