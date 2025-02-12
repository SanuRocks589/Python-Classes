def total_calc(total_bill, tip_perc):
    total = ((total_bill*tip_perc)//100) + total_bill
    print("You need to pay $", total)

total_bill = int(input("What is the bill amount:"))
tip_perc = int(input("What is the tip percentage:"))
total_calc(total_bill, tip_perc)