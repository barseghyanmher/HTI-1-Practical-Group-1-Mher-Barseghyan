def uppercase():

    check_word = word.isupper()

    return check_word


word = input("Input a text :")

if uppercase():
    print("Yes")
else:
    print("No")
