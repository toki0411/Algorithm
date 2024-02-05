str = input()
target = input();
targetlen = len(target)
s = []
for i in range(len(str)):
    s.append(str[i])
    if ''.join(s[-targetlen:]) == target:
        for j in range(targetlen):
            s.pop();


if s:
    print(''.join(s))
else:
    print("FRULA")

