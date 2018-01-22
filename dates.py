#2.5 Days Between Dates.py

# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

#if (year is not divisible by 4) then (it is a common year)
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)

# def functions():
#     functions = ['isLeapYear(year)', 'daysInMonth(month, year)', 
#                  'nextDay(year, month, day)', 'targetDate(year, month, day, days)', 
#                  'dateIsBefore(year1, month1, day1, year2, month2, day2)', 
#                  'daysBetweenDates(year1, month1, day1, year2, month2, day2)']
#     for i in functions:
#         print i
#     return


def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def daysInMonth(month, year):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        days[1] = 29
    return days[month - 1]


def nextDay(year, month, day):
    if day < daysInMonth(month, year):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


# So I need to lose 71 lbs to be under 200...if I wanted to lose 
# at 2 lbs/week what would the date be?

def targetDate(year, month, day, days):
    count = 0
    while count != days:
        year, month, day = nextDay(year,month,day)
        count += 1
    return year, month, day

#print targetDate(2016,11,4,38)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    date1 = str(month1) + '/' + str(day1) + '/' + str(year1)
    date2 = str(month2) + '/' + str(day2) + '/'+ str(year2)
    days_per_month = 365.25 / 12
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    print (str(days) + ' days between ' + date1 + ' and ' + date2 + '\n' +
    str(round(days / days_per_month, 1)) + ' months between ' + date1 + ' and ' + date2)

daysBetweenDates(2019,4,29,2020,4,29)


#def test():
#    test_cases = [((2012,1,1,2012,2,28), 58), 
#                  ((2012,1,1,2012,3,1), 60),
#                  ((2011,6,30,2012,6,30), 366),
#                  ((2011,1,1,2012,8,8), 585 ),
#                  ((1900,1,1,1999,12,31), 36523)]
#    
#    for (args, answer) in test_cases:
#        result = daysBetweenDates(*args)
#        if result != answer:
#            print "Test with data:", args, "failed"
#        else:
#            print "Test case passed!"
#
#test()