def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    # check if command is valid, either "remove" or "add"
    if command not in ("remove", "add"):
        return None
    
    # check if location is valid, either "beginning" or s"end"
    if location not in ("beginning", "end"):
        return None
    
    # execute actions based in command and location
    if command == "remove":
        if location == "beginning":
            return lst.pop(0)
        else: 
            return lst.pop()
    else:
        if value is None:
            return None
        if location == "beginning":
            lst.insert(0, value)
        else:
            lst.append(value)
        return lst

    # if command == "remove":
    #     if location == "end":
    #         return lst.pop()
    #     elif location == "beginning":
    #         return lst.pop(0)

    # elif command == "add":
    #     if location == "beginning":
    #         lst.insert(0, value)
    #         return lst
    #     elif location == "end":
    #         lst.append(value)
    #         return lst
    
lst = [1, 2, 3]
print(list_manipulation(lst, 'add', 'beginning', 20))
print(list_manipulation(lst, 'add', 'end', 30))
print(lst)
print(list_manipulation(lst, 'foo', 'end'))
print(list_manipulation(lst, 'add', 'dunno'))
