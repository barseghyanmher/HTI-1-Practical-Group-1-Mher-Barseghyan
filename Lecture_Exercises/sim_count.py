def commonCharacterCount(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    count = 0
    for i in s1_list:
        for s in s2_list:
            if i == s:
                count += 1
                s2_list.remove(s)
                break
    return count
