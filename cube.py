def cube(num):
    return num**3
def func(num):
    if num%3 == 0:
        return cube(num)
    else:
        return False
num = int(input("What is the number you would like to cube:"))
print (func(num))