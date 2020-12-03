num = int(input("Enter number 2<num<500 :"))
fac = 1
for i in range(2, num+1):
    print(i)
    fac *= i
print(fac)
