from itertools import *
def solution(users, emoticons):
    join = profit = 0
    n = len(emoticons);
    case = list(product([10, 20, 30, 40], repeat = n))
    for c in case: #(10,10,20,10)
        plus = purchase =  0
        for u in users:
            price = 0
            percent , limit = u
            for i in range(n):
                if c[i] >= percent:
                    price += int((100-c[i])*0.01*emoticons[i])
            if price >= limit:
                plus += 1
                price = 0
            purchase += price
        if plus > join :
            join = plus
            profit = purchase
        elif plus == join and purchase > profit:
            profit = purchase

    return [join, profit]