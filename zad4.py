def div(start, end):
    return [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 != 0]


print(div(0, 14))
