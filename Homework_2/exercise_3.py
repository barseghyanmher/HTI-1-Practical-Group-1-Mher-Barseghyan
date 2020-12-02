number = input("Input a number :")
numbers = [int(i) for i in number]


def possible(lst):
    is_possible = False
    while lst:
        num = lst[0]
        for i in lst[1:]:
            if num < i:
                is_possible = True
                break
        if is_possible:
            break
        lst = lst[1:]
    return is_possible


if possible(numbers):
    print('Yes')
else:
    print('No')
