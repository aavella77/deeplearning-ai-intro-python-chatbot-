from datetime import date

def days_between(date1, date2):
	"""Calculates the number of days between two dates."""
	return (date2 - date1).days

# Your birthday
birthday = date(date.today().year, 10, 5)

# Christmas
christmas = date(date.today().year, 12, 25)

# Calculate the number of days between Christmas and your birthday
days_to_birthday_from_christmas = days_between(christmas, birthday)

# Handle case where birthday is before Christmas in the same year
if days_to_birthday_from_christmas < 0:
	days_to_birthday_from_christmas += 365

print(f"Days between Christmas and your birthday: {days_to_birthday_from_christmas}")