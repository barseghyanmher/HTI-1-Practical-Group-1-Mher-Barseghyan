def merge(l1, l2):
    lst = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            lst.append(l2[j])
            j += 1
        else:
            lst.append(l1[i])
            i += 1
    if i < len(l1):
        lst.extend(l1[i:])
    elif j < len(l2):
        lst.extend(l2[j:])
    return lst


lst1 = [1, 3, 4, 6, 8, 12]
lst2 = [2, 4, 5, 5, 6, 7, 10, 11]
print(merge(lst1, lst2))
