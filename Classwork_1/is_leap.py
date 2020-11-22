year_num = int(input("Your Birth Year :"))
if year_num % 4 != 0:
    print("No")
elif year_num % 4 == 0 and year_num % 100 != 0:
    print("Yes")
elif year_num % 4 == 0 and year_num % 100 ==0 and year_num % 400 ==0:
    print("Yes")
else:
    print("No")