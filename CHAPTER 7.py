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
    test(sum_even_nofirst(mylist)==-16)
    test(sam(mylist2)==5)
    
mylist=[-13,-3,0,2,3,7,11,12]
mylist2=["apple", "banana","watermelon","grape","sam","pear","orange"]
def count_odd(numlist):
    count=0
    for n in numlist:
        if n%2 !=0:
            count+=1
    return count
    
def sum_even(numlist):
    sum=0
    for n in numlist:
        if n%2 == 0:
            sum=sum+n
    return sum

def sum_neg(numlist):
    sum=0
    for n in numlist:
        if n < 0:
            sum=sum+n
    return sum


def count_words(numlist):
    count=0
    for n in numlist:
        if len(n)==5:
            count+=1
    return count
    
def sum_even_nofirst(numlist):
    sum=0
    for n in numlist:
        if n%2 == 0:
            break
        else:
            sum+=n
    return sum

def sam(numlist):
    count=0
    for i in numlist:
        if i == "sam":
            count += 1
            break
        else:
            count += 1
    return count
        
    
test_suite()
print(count_odd(mylist))
print(sum_even(mylist))
print(sum_neg(mylist))
print(count_words(mylist2))
print(sum_even_nofirst(mylist))
#Sum all the elements in a list up to but not including the first even number.  (Write your unit tests. What if there is no even number?) 
#Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)
