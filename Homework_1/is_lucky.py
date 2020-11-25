i = input("Enter thr number with pair elements :")
a = len(i) // 2
part1 = int(i) % 10 ** a
part2 = int(i) // 10 ** a
# print(part1, part2)
sum1 = 0
while part1 != 0:
    digit1 = part1 % 10
    if digit1 != 0:
        sum1 = sum1 + digit1
    part1 = part1 // 10
sum2 = 0
while part2 != 0:
    digit2 = part2 % 10
    if digit2 != 0:
        sum2 = sum2 + digit2
    part2 = part2 // 10
# print(sum1, sum2)
if sum1 == sum2:
    print("Yes")
else:
    print("No")
