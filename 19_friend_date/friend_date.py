def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """

    a_hobbies = a[2]
    b_hobbies = b[2]

    common_hobbies = set(a_hobbies) & set(b_hobbies)

    return len(common_hobbies) > 0

    # if set(a[2]) & set(b[2]):
    #     return True
    # else:
    #     return False

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 
10000, ['waving wands', 'chess'])

print(friend_date(elmo, sauron))
print(friend_date(sauron, gandalf))
