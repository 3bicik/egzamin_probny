def dividers(number):
    result = []
    for i in range(1, number+1):
        if number % i == 0:
            result.append(i)
    return result


print(dividers(6))
