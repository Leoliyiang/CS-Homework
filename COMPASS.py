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
    test(turn_clockwise("N")=="S")



def turn_clockwise(dire):
    if dire == "N":
        return "E"
    elif dire == "E":
        return "S"
    elif dire == "S":
        return "W"
    elif dire == "W":
        return "N"
    else:
        return None

test_suite()
