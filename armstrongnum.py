num = int(input("Enter any 3-digit number to check if it is an armstrong number:"))
sum = 0 
arm = num

while arm>0:
    dig = arm%10
    sum = sum+dig**3
    arm = arm//10
if num==sum:
    print("Yes, it's an armstrong number!!")
else:
    print("Your number isn't an armstrong number.")