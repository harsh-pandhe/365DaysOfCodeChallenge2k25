def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def next_leap_years(start_year, count=5):
    leap_years = []
    year = start_year
    while len(leap_years) < count:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1
    return leap_years


year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year! 🌟")
else:
    print(f"{year} is not a leap year.")
leap_years = next_leap_years(year)
print(f"The next {len(leap_years)} leap years after {year} are: {leap_years}")
