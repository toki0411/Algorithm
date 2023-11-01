for _ in range(4):
    first_x, first_y, first_p, first_q, second_x, second_y, second_p, second_q = list(map(int, input().split()))
    #만나지 않음
    if first_p < second_x or first_x > second_p or first_q < second_y or first_y > second_q:
        print('d'); continue
    #점
    elif (first_x == second_p and first_y == second_p) or (first_p == second_x and first_y == second_q) or (first_p == second_x and first_q == second_y) or (first_x == second_p and first_q == second_y):
        print('c'); continue
    elif first_p == second_x or first_x == second_p or first_y == second_q or first_q == second_y:
        print('b'); continue
    else:
        print('a')
