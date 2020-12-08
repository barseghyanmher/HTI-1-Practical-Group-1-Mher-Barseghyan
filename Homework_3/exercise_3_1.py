def missing_num(nums):
    is_swapped = True
    n = len(nums)
    while is_swapped:
        is_swapped = False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_swapped = True
        n -= 1

    missed_num = 0
    for i in nums:
        if nums[i + 1] - nums[i] != 1:
            missed_num = nums[i] + 1
            break

    return missed_num


numbers = [int(i) for i in input("Enter N-1 numbers whit space :").split()]
print(missing_num(numbers))
