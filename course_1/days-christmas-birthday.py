from datetime import date

def days_between(date1, date2):
	"""Calculates the number of days between two dates."""
	return (date2 - date1).days

# Your birthday
birthday = date(1971, 10, 5)

# Christmas
christmas = date(date.today().year, 12, 25)

# Handle case where Christmas has already passed this year
if christmas < date.today():
	christmas = date(date.today().year + 1, 12, 25)

days_to_christmas = days_between(date.today(), christmas)

# Handle case where birthday has already passed this year
next_birthday = date(date.today().year, birthday.month, birthday.day)
if next_birthday < date.today():
	next_birthday = date(date.today().year + 1, birthday.month, birthday.day)

days_to_birthday = days_between(date.today(), next_birthday)

print(f"Days until Christmas: {days_to_christmas}")
print(f"Days until your birthday: {days_to_birthday}")