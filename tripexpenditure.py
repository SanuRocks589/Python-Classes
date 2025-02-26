#Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip

def hotel_cost(nights):
    return 3000*nights
def plane_cost(city):
    if "delhi"== city:
        return 7000
    elif "lucknow" == city:
        return 5000
    elif "banglore" == city:
        return 13000
def vehicle_cost(days):
    if days>4:
        return 2000*days
    elif days<4:
        return 3000*days
def trip_expenditure(nights, days, city, extra_money):
    return hotel_cost(nights) + plane_cost(city) + vehicle_cost(days) + extra_money

nights = int(input("How many nights are you staying:"))
days = nights + 1 
city = input("What city would you like to go to (banglore/delhi/lucknow):")
extra_money = int(input("Enter any extra amount of money you have used:"))
print(f"Your total trip expenditure is {trip_expenditure(nights, days, city, extra_money)}")
