def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    # new_list = []

    # for i in range(0, len(lst), 2):
    #     new_list.append(lst[i])
    
    # return new_list

    return lst[::2]

lst = [1, 2, 3, 4, 5]


print(remove_every_other(lst))
print(lst)


    