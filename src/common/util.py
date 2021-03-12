import os
if os.getenv("DEBUG"):
    import pdb

''' common infrastructure that helps the logic of the api '''
# pdb.set_trace()


def largest_palindrome(phrase):
    ''' Is a function to find the largest palindrome from the string,
    the rules for finding this type of sub string is:
     - Spaces are considered here as well as upper and lower case.
     - Blank spaces are not eliminated.
     - Case is case sensitive.
     - Characters are not replaced in strings
    return: the largest palindrome and if it is two, it returns the first answear
    The time complexity is n^2
    '''
    # if is not a string and it is a number, pass to string and see if the
    # number is palidrome
    if type(phrase) in (int, float):
        phrase = str(phrase)

    if not type(phrase) is str:
        return None

    lenght = len(phrase)
    if lenght == 0:
        return None

    if lenght == 1:
        return phrase

    # start counting to the last number of the list
    for reverse_n in range(lenght, 0, -1):
        # start counting the last number
        for start_n in range(lenght - reverse_n + 1):

            # var for check the end of the string
            finish = start_n < 1 if None else start_n - 1

            # the -1 revert the list compare the string normal with the revert string
            normal = phrase[start_n: start_n + reverse_n]
            reverse = phrase[start_n + reverse_n - 1: finish: - 1]

            if reverse == normal:
                return normal

    # when it doesnt find nothing
    return None
