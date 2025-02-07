def sqr(a):
    peris = 4*a
    print(peris, "is the perimeter of the square.")
def rec(a,b):
    perir = 2*(a+b)
    print(perir, "is the perimeter of the rectangle.")
def cir(a):
    circum = 2*3.14*a
    print(circum, "is the circumfrence of the circle.")
def tri(a,b,c):
    perit = a+b+c
    print(perit, "is the perimeter of the triangle.")

print("Which of the shapes would you like to find the perimeter of?")
print("a. Square")
print("b. Rectangle")
print("c. Circle")
print("d. Triangle")
inp = input("Enter any (a,b,c,d):")

if inp == "a":
    a = int(input("Enter the length of one side of the square:"))
    sqr(a)
elif inp == "b":
    a = int(input("Enter the length of the rectangle:"))
    b = int(input("Enter the breadth of the rectangle:"))
    rec(a,b)
elif inp == "d":
    a = int(input("Enter the length of first side:"))
    b = int(input("Enter the breadth of the second side:"))
    c = int(input("Enter the breadth of the third side:"))
    tri(a,b,c)
elif inp == "c":
    a = int(input("Enter the length of the radius of the circle:"))
    cir(a)