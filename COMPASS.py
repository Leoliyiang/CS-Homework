import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    pass
    print("turn_clockwise")
    test(turn_clockwise("N")=="S")
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)


    print("\ndays_in_month")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    print("\nday to name")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    
    print("\nday name to number")
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    
    print("\nday_add")
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    
    
    
    print("9. Reverse Hours")
    test(hours_in(9019) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

    print("even?")
    test(is_even(8.3) == False)
    test(is_even(8) == True)
    
    print("odd?")
    test(is_odd(3) == True)

    print("factor?")
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    print("multiple?")
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    
    print("tem?")
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)

    print("tem c?")
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)
    
    print("prime?")
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))

    
def turn_clockwise(direction):
    """takes a compass point and return the next clockwise point"""
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
   

def day_name(num):
    """takes a day number 0-6 and return the name"""
    if num == 0:
        return "Sunday"
    if num == 1:
        return "Monday"
    if num == 2:
        return "Tuesday"
    if num == 3:
        return "Wednesday"
    if num == 4:
        return "Thursday"
    if num == 5:
        return "Friday"
    if num == 6:
        return "Saturday"
    else:
        return None

def day_num(day_name):
    """takes a day name and returns a number 0-6"""
    if day_name == "Sunday":
        return 0
    elif day_name ==  "Monday":
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == 6:
        return 6
   

def day_add(name,delta):
    """takes in a day name and a number of days (delta). Adds the delta - returns name of the day."""
    start_day_num = day_num(name)
    end_day_num = start_day_num + delta
    end_day_name = day_name(end_day_num % 7)
    return end_day_name


def days_in_month(name):
    """takes a month name and returns the number of days in that month"""
    if name == "January" or name == "March" or name == "May" or name == "July" or name == "August" or name == "October" or name == "December":
        return 31
    elif name == "February":
        return 28
    elif name == "April"  or name == "June"  or name == "November":
        return 30

def hours_in(secs):
    return secs//3600

def minutes_in(secs):
    return secs%3600//60

def seconds_in(secs):
    return secs%3600%60

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def is_odd(n):
    if is_even(n):
        return False
    else:
        return True
#3   if n%2 == 0:
#      return False
#    else:
#        return True

def is_factor(f,n):
    if n%f == 0:
        return True
    else:
        return False

def is_multiple(a,b):
    return is_factor(b,a)
    
def f2c(t):
    return round((t-32)/1.8,0)

def c2f(tc):
    return round((tc*1.8+32), 0)
    #if a%b == 0:
     #   return True
    #else:
     #   return False
     
def sqrt(n):
    """Ex 7:Newtons square root function -"""
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("better",better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


print("sqrt",sqrt(25.0))

def is_prime(n):
    """Write a function, is_prime, which takes a single integer
    argument and returns True when the argument is a prime number and False otherwise"""
    for i in range(2,n):
        if n % i == 0:
            return False
    return True



print(sqrt(25))
test_suite()
