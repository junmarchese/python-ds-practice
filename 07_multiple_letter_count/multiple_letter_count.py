def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # letter_counter = {}
    # for letter in phrase:
    #     if letter.isalpha:
    #         if letter in letter_counter:
    #             letter_counter[letter] += 1
    #         else: 
    #             letter_counter[letter] = 1
    # return letter_counter

    counter = {}
    for letter in phrase:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))

