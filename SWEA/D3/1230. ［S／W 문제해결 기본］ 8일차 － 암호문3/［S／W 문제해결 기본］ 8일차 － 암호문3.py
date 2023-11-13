

for tc in range(1, 11):
    input()
    data = list(input().split())
    input()
    command = input().split()
    for i in range(len(command)):
        if command[i] == 'I':
           x = int(command[i+1])
           y = int(command[i+2])
           for l in range(y):
               data.insert(x+l, command[l+i+3])
        elif command[i] == 'D':
            x = int(command[i+1])
            y = int(command[i+2])
            for l in range(y):
                del data[x]

        elif command[i] == 'A':
            y = int(command[i+1])
            for l in range(y):
                data.append(command[i+l+2])

    print('#{} {}'.format(tc, ' '.join(data[:10])))