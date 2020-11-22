a = int(input("Enter a number :"))
b = int(input("Enter a number :"))
c = int(input("Enter a number :"))

if a >= b and a >= c:
    c,a = a,c

elif b >= a and b >= c:
    b,c = c,b

if c>= a + b:
    print("Not a triangle")
elif c*c == a*a + b*b:
    print("Right triangle")
elif c*c < a*a + b*b:
    print("Acure triangle")
else:
    print("Obtuse triangle")

