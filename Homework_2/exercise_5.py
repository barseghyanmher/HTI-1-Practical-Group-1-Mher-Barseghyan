numbers = input("Enter heights with space :").split()
new = [int(i) for i in numbers]


def sum_num(lst):
    new_list = []
    max_num = max(lst)
    for i in lst:
        i = max_num - i
        new_list.append(i)
    summ = sum(new_list)
    return summ


print(sum_num(new))
