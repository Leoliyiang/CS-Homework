''' I DIND'T FINISH THIS ONE, PLZ DON'T GRADE THIS
    BUT COULD YOU SEE WHAT PROBLEMS DO I HAVE?'''


import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def reverse(word):
    rw=""
    n=0
    while n < len(word):
        ch=word[len(word)-1-n]
        n += 1
        rw+=ch
    return rw

def is_palindrome(word_pa):
    if word_pa == reverse(word_pa):
        return True
    return False

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
# test(is_palindrome(""))    # Is an empty string a palindrome?'''