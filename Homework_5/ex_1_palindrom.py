def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

    # return text[0] == text[-1] and is_palindrome(text[1:-1])


if is_palindrome(input('Enter a text: ')):
    print('Yes')
else:
    print('No')
