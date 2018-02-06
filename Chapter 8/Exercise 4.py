def count_letters(word,itr):
    count=0
    repeats=0
    while repeats < len(word):
        str_index = word.find(itr,repeats,repeats+1)
        if str_index >= 0:
            count += 1
        repeats +=1

    return count
print(count_letters("banana","a"))