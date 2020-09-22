"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""
    
    count = 0
    while lst:
        count +=1
        lst = lst[0:-1]
        count_recursively(lst)
    return count


    count_recursively(lst)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
