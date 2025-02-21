import random 

number = str(random.randint(0, 10))
given = int(input("Enter a random number from 0,10:"))

if given == number:
    print("You have guessed correctly, the number was indeed", number)
else:
    print("Nice try but you have guessed wrong, the number was actually", number)