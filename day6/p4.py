from datetime import date, datetime

# Current date and time
now = datetime.now()
print("Current datetime:", now)

# Specific date
my_date = date(2024, 10, 7)
print("Specific date:", my_date)

# Only date part
print("Only date:", now.date())

# Only time part
print("Only time:", now.time())