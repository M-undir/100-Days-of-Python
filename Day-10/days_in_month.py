def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_chosen, month_chosen):
    if month_chosen < 1 or month_chosen > 12:
        return "Please input a month between 1 and 12"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_chosen):
        month_days[1] = 29
    return month_days[month_chosen]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: ")) - 1
days = days_in_month(year, month)
print(days)