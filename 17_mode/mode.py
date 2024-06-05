def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    nums_counter = {}

    for num in nums:
        if num in nums_counter:
            nums_counter[num] += 1
        else:
            nums_counter[num] = 1
    
    highest_count = 0
    most_frequent_num = None
    for num, count in nums_counter.items():
        if count > highest_count:
            highest_count = count
            most_frequent_num = num

    return most_frequent_num


    # counts = {}

    # for num in nums:
    #     counts[num] = counts.get(num, 0) + 1

    # max_value = max(counts.values())

    # for (num, freq) in counts.items():
    #     if freq == max_value:
    #         return num


print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))

