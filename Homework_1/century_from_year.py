year = int(input("Enter yor birth year: "))
cent = year // 100
if year % 100 != 0:
    cent = cent + 1
print(cent)
