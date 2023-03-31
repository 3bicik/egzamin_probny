def name_sorter(names):
    sorted_names = {
        "male": [],
        "female": []
    }
    for name in names:
        if name[-1].lower() == "a":
            sorted_names["female"].append(name)
        else:
            sorted_names["male"].append(name)
    return sorted_names


print(name_sorter(["Dawid", "Anna", "Hubert", "Radek", "Dominika", "Justyna", "Michał"]))
