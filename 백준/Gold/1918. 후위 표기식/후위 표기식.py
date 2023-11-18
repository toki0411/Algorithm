str = list(input())
st = []
res = []
for s in str:
    if s.isalpha():
        res.append(s)
    else:
        if s == '(':
            st.append(s)
        elif s == '*' or s == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                res.append(st.pop())
            st.append(s)
        elif s == '+' or s == '-':
            while st and st[-1] != '(':
                res.append(st.pop())
            st.append(s)
        elif s == ')':
            while st and st[-1] != '(':
                res.append(st.pop())
            st.pop()
while st:
    res.append(st.pop())
print(''.join(res))

