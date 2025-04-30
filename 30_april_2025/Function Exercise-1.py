def sumlist(list):
    y = 0
    for x in list:
        y = x + y
    return y

list = [8, 2, 3, 0, 7]

print(sumlist(list))