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


def merge_sort(lst, start, end):
    if start == end - 1:
        return lst[start:end]
    mid = (start + end) // 2
    return merge(merge_sort(lst, start, mid), merge_sort(lst, mid, end))


nums = [6, 3, 2, 5, 5, 0, 0, 2, 4, 6, 3, 9, 1]
print(merge_sort(nums, 0, len(nums)))
