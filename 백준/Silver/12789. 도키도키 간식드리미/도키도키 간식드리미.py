n = int(input())
student = list(map(int, input().split()))
index = 1
st = []
key = False
while True:
    if index > n:
        break;
    elif len(st) > 0 and st[-1] == index:
        st.pop();
        index+=1
    elif len(student)>0 and student[0] == index:
        del student[0]
        index += 1
    elif len(student)>0 :
        st.append(student[0])
        del student[0]
    elif len(st) > 0 and st[-1] != index:
        key = True;
        break;

if key:
    print("Sad")
else :
    print("Nice")