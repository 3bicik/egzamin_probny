def shorten(text):
    words = text.split()
    short = ""
    for word in words:
        short += word[0].upper()
    return short


print(shorten("Zadanie pierwsze test"))
