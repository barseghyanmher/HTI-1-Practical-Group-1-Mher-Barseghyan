number = int(input("Enter a pair number :"))
num_list = [int(i) for i in range(1, number+1)]


def prime(num):
    prime_flag = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime_flag = False
            break
    return prime_flag


for num1 in num_list[1:]:
    if prime(num1):
        num2 = number - num1
        if prime(num2):
            print(num1, num2)
            break
