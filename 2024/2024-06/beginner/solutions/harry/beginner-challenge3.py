
def sum(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    return sum


print(sum([11, 12, 33, 19, 82, 101]))
