import re
import sys


def valid_email():
    email = input("Input Email: ")
    if re.match("[^@]+@[^@]+\.[^@]+", email):
        return print("True")
    else:
        return print("False")

def valid_phone_num():
    phone_num = input("Input phone number: ")
    if re.match("^0{0,1}(77|55|99|98|91)([\ ]|[-]{0,1})((([0-9]{3})([\ ]|[-]{0,1})([0-9]{3}))|((([0-9]{2})([\ ]|[-]{1})([0-9]{2})([\ ]|[-]{1})([0-9]{2}))|(([0-9]{6}))))$", phone_num):
        return print("True")
    else:
        return print("False")

if __name__ == '__main__':
    commands = {
        'email': valid_email(),
        'phone_num': valid_phone_num(),
    }

    # func = commands.get(sys.argv)
    # if func:
    #     func(sys)
