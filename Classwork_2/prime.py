def prime(num):

    prime_flag = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime_flag = False
            break
    return prime_flag


number = int(input("Enter number:"))

if prime(number):
    print("Yes")
else:
    print("No")
