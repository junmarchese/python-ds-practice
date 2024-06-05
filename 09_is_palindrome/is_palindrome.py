def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    # case_insensitive_phrase = "".join(char.lower() for char in phrase if char.isalnum())
    # return case_insensitive_phrase == case_insensitive_phrase[::-1]

    normalized = phrase.lower().replace(" ", "")
    return normalized == normalized[::-1]

print(is_palindrome('tacocat'))
print(is_palindrome('noon'))
print(is_palindrome('robert')) 
print(is_palindrome('taco cat'))
print(is_palindrome('Noon'))
