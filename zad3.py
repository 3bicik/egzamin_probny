def check_palindrome(text):
    if text.lower() == text[::-1].lower():
        return True
    return False

print(check_palindrome("Kajak"))
print(check_palindrome("Woda"))