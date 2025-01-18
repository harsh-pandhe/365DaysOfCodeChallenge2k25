# 🎯 Day #18 of My 365 Days Coding Challenge!  

---

## 💭 **A Personal Reflection:**  
Time is fascinating, especially when it comes to leap years. These extra days keep our calendars aligned with Earth’s orbit. Today’s task reminded me how even small programming challenges can help us understand the logic behind everyday phenomena.  

---

## 📚 **What I Did Today:**  
I wrote a Python program to determine if a year is a leap year. Leap years occur every 4 years, except for years divisible by 100 but not 400.  

---

### Code:  

```python
# leap_year.py
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year! 🌟")
else:
    print(f"{year} is not a leap year.")
```

---

## 💡 **Key Learning:**  
This task demonstrated how combining simple conditions can solve real-world problems. It’s also a reminder of how programming makes abstract rules tangible.  

---

## ✨ **Extra Touch:**  
I extended the program to calculate the next 5 leap years starting from the given year:  

```python
def next_leap_years(start_year, count=5):
    leap_years = []
    year = start_year
    while len(leap_years) < count:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1
    return leap_years

year = int(input("Enter a year: "))
leap_years = next_leap_years(year)
print(f"The next {len(leap_years)} leap years after {year} are: {leap_years}")
```

---

## 🚀 **Your Turn:**  
- Can you extend this program to calculate the number of leap years between two given years?  
- Bonus: Try creating a function that calculates the total number of leap years in a century!  

---

#365DaysOfCode #CodingChallenge #LeapYear