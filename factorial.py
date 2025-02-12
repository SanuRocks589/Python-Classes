def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

num = int(input("What is the number you would like to find factorial of:")) 
print(factorial.__doc__)
print("This is the result:", factorial(num))