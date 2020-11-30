def get_sum(n):
    summ = 0
    for digit in str(n):
        summ += int(digit)
    return summ


number = input("Input a number :")

sum1 = get_sum(number)
while sum1 >= 10:
    sum1 = get_sum(sum1)
print(sum1)
