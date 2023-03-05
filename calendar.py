n = 0

def leap_year(y):
    if y % 4 == 0 and y%100 != 0:
        return 1
    elif y % 400 == 0:
        return 1
    else:
        return 0
def number_of_days(m, y):
    if leap_year(y) == 1 and m == 2:
        return 29
    if m == 2:
        return 28
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30

def days_passed(d, m, y):
    global n 
    for i in range(1, m):
        n += number_of_days(i, y)
    return n + d - 1
   
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))


options = int(input("Menu:\n1) Calculate the number of days in the given month. \n2) Calculate the number of days passed in the given year. "))


o1 = number_of_days(month, year)
o2 = days_passed(day, month, year)

if options == 1:
    print(o1)
if options == 2:
    print(o2)


