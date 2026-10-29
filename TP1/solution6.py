#Exercise 6 Leap Day in a month 
def is_leap(year):
    return( year % 4 ==0 and year % 100 != 0 ) or (year%400==0)

def day_in_month(month,year):
    if month <1 or month >12:
        return None
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in(4,6,9,11):
        return 30
    else:
        return 31
years_test=[1900,2000,2024,2026]
for y in years_test:
    if is_leap(y):
        print(f"{y} Is leap")
    else:
        print(f"{y} Is not leap")
print(f"Feb 2024 :{day_in_month(2,2024)}| Feb 2026:{day_in_month(2,2026)}|Apr: {day_in_month(30,2000)} |month 13: {day_in_month(13,2000)}")

leap_count=0
for year in range (2000,2101):
    if is_leap(year):
        leap_count += 1

        print(f"This is the leap days:{leap_count}")
