def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]
print(reverse_string('awesome'))
print(reverse_string('sauce'))


#     #reverse string by converting it into a list
#     myList = list(phrase)
#     myList.reverse()
#     phrase = "".join(myList)
#     return phrase

# print(reverse_string('awesome'))
# print(reverse_string('sauce'))




#     #reverse string using string slicing
#     phrase = phrase[::-1]

#     return phrase

# print(reverse_string('awesome'))
# print(reverse_string('sauce'))



#     #reverse string using reversed() method
#     phrase = "".join(reversed(phrase))

#     return phrase

# print(reverse_string('awesome'))
# print(reverse_string('sauce'))



#     #reverse string using recursion
#     if len(phrase) == 0:
#         return phrase
    
#     else:
#         return reverse_string(phrase[1:]) + phrase[0]
    
# print(reverse_string('awesome'))
# print(reverse_string('sauce'))
    
    
    
#reverse string using simple for-loop
#     reversedString = ""

#     for char in phrase:
#         reversedString = char + reversedString
#     return reversedString
    
# print(reverse_string('awesome'))
# print(reverse_string('sauce'))
