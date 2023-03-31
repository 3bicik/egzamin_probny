def get_initials(name_list):
    result = []
    for name_surname in name_list:
        initials = name_surname.split()[0][0] + name_surname.split()[1][0]
        # name = name_surname.split()[0]
        # surname = name_surname.split()[1]
        result.append(initials)
    return result


print(get_initials(["Jan Kowal", "Adam Nowak"]))