import calendar

cal = calendar.TextCalendar(firstweekday=3)      # part b
cal.pryear(2012)
cal.prmonth(1999,12, w=0, l=0) #part c
d = calendar.LocaleTextCalendar(6, "CHINESE") #part d
d.pryear(2012)

print(calendar.isleap(2012)) #part d Returns True if year is a leap year, otherwise False. It's called conditional function
print(type(calendar.isleap))
