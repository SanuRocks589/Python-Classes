num = int(input("Enter any number to find its factorial:"))
i=1
factorial = 1

while i<=num:
    factorial = factorial * i
    i=i+1
print(factorial)