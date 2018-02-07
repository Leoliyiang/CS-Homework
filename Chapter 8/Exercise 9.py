import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def remove_letter(ch,word):
    sentence = ""
    for l in word:
        if l != ch:
            sentence += l
    return sentence


test(remove_letter("a", "apple") == "pple")
test(remove_letter("a", "banana") == "bnn")
test(remove_letter("z", "banana") == "banana")
test(remove_letter("i", "Mississippi") == "Msssspp")
test(remove_letter("b", "") == "")
test(remove_letter("b", "c") == "c")

'''textbook is wrong, it wrote test(remove_letter("b", "") = "")
                               test(remove_letter("b", "c") = "c")
    but the "=" should be "==", please fix the textbook!!!!!!!!!!!!'''