def missing_num(nums):
    max_num = max(nums)
    lst = list(range(max_num + 1))
    if sum(nums) == sum(lst):
        missed_num = max_num + 1
    else:
        missed_num = sum(lst) - sum(nums)
    return missed_num


numbers = [int(i) for i in input("Enter N-1 numbers whit space :").split()]
print(missing_num(numbers))
