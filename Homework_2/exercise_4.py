number = input("Input a number :")
main_list = [int(i) for i in number]


def odd_indexs(lst):
    odd_indexs_lst = []
    for i in range(1, len(lst), 2):
        odd_indexs_lst += [(lst[i])]
    return odd_indexs_lst


def pair_indexs(lst):
    pair_indexs_lst = []
    for i in range(0, len(lst), 2):
        pair_indexs_lst += [(lst[i])]
    return pair_indexs_lst


sum_odd = sum(odd_indexs(main_list))
sum_pair = sum(pair_indexs(main_list))

if sum_odd == sum_pair:
    print("Yes")
else:
    print("No")
