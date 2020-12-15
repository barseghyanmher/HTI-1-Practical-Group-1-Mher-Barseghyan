def chart_count():
    my_string = input("Input somthing: ")
    my_dict = {}
    for letter in my_string:
        if letter not in my_dict.keys():
            my_dict[letter] = 1
        else:
            my_dict[letter] += 1

    return my_dict


print(chart_count())
