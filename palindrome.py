def palindrome(x):
    y =  len(x) - 1
    z = 0 
    while (z<y):
        if (x[z] != x[y]):
            return False
        z+=1
        y-=1
    return True

tuples = (1,2,3,2,1)
if (palindrome(tuples)):
    print("It's a palindrome.")
else:
    print("This tuple is not a palindrome.")