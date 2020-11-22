year = int(input("Enter your Year :"))
multiple = 1
while year != 0:
    digit = year % 10
    if digit != 0:
        multiple = multiple * digit
    year = year // 10
print(multiple)



