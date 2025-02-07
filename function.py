def add(x, y):
    return x+y 

def sub(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x, y):
    return x/y

print("Choose your operation")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
inp = input("Enter here (a,b,c,d):")
x = int(input("Enter first number:"))
y = int(input("Enter another number:"))
if inp == "a":
    print(x,"+", y, "=", add(x,y))
elif inp == "b":
    print(x,"-", y, "=", sub(x,y))
elif inp == "c":
    print(x,"*", y, "=", mult(x,y))
elif inp == "d":
    print(x,"/", y, "=", div(x,y))
else: 
    ("Please try again choosing options a,b,c or d.")