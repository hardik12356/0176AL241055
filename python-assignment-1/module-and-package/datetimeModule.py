import datetime

# Current Date and Time
now = datetime.datetime.now()
print("Current Date:", now.date())
print("Current Time:", now.time())

# Calculate Age
dob = input("Enter date of birth (YYYY-MM-DD): ")
dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()

today = datetime.date.today()
age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Age:", age)