num =int(input("Enter number of days: "))

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("Number of years=", year)
print("Number of weeks=", week)
print("Number of days=", days)