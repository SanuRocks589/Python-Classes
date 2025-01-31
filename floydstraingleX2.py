print("Here is the floyds triangle:")
rows = int(input("Enter the number of rows:"))
prf = 1

for i in range(rows):
    for j in range (i+1):
        print(prf, end=" ")
        prf = prf*2
    print()