from datetime import date, datetime, time

today = date.today()
now = datetime.now().strftime("%H:%M:%S")
print(f"It is {now}, and today is {today}.")