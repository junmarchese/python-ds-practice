def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    counter = 0
    for item in lst:
        if item == search_term:
            counter += 1
    return counter

    # return lst.count(search_term)

print(frequency([1, 4, 3, 4, 4], 4))
print(frequency([1, 4, 3], 7))
print(frequency([1, 2, 5, 8, 5, 9, 5, 5], 5))
print(frequency(["apple", "banana", "custard"], "custard"))
print(frequency(["apple", "banana"], "custard"))
