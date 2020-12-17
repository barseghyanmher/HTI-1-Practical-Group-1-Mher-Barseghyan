def revers_tall(l, reversed_l = []):
    if not l:
        return reversed_l
    return revers_tall(l[1:], [l[0]] + reversed_l)


def revers_list(l):
    if not l:
        return []
    return revers_list(l[1:]) + [l[0]]


print(revers_list([1, 2, 3, 4]),  revers_tall([1, 2, 3, 4]))
