def print_reverse(n):
    if not n:
        return
    num = int(input())
    print_reverse(n - 1)
    print(num)


N = int(input())
print_reverse(N)
