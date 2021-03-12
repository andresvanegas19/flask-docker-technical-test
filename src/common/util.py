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
    for reverse_n in range(len(phrase), 0, -1):
        # start counting the last number
        for start_n in range(len(phrase) - reverse_n + 1):

            # var for check the end of the string
            finish = start_n < 1 if None else start_n - 1

            # the -1 revert the list compare the string normal with the revert string
            reverse = phrase[start_n + reverse_n - 1: finish: - 1]
            normal = phrase[start_n: start_n + reverse_n]

            if reverse == normal:
                return normal

    # when it doesnt find nothing
    return None


if __name__ == '__main__':
    """
    This is for making quick testing of the function
    """
    print(largest_palindrome(""))  # None
    print(largest_palindrome("erre"))  # None
    print(largest_palindrome("new"))  # n
    print(largest_palindrome("newen"))  # newen
    print(largest_palindrome("kayak"))  # None
    print(largest_palindrome("abba"))  # abba
    print(largest_palindrome("a"))  # a
    print(largest_palindrome("abcc"))  # cc
    print(largest_palindrome("Anita lava la tina"))  # ava
    print(largest_palindrome("12345654321"))  # 12345654321
    print(largest_palindrome("abaaaa"))  # aba
    print(largest_palindrome("n "))  # n_
    print(largest_palindrome("perl lrep"))  # perl lrep
    print(largest_palindrome("abcda"))  # abcda
    print(largest_palindrome("n n"))  # n n
    print(largest_palindrome("U+006- U+01"))  # 00
    print(largest_palindrome("/@[#-;!;$#Q"))  # ;!;
    print(largest_palindrome("d     sadas       ie"))  # space sadas space
    print(largest_palindrome("1-2-3-4 4-3-2-1"))  # 1-2-3-4 4-3-2-1
    print(largest_palindrome("passion"))  # ss
    print(largest_palindrome(None))  # None
    print(largest_palindrome("three"))  # ee
    print(largest_palindrome("tw"))  # tw
    print(largest_palindrome("éné"))  # éné
    print(largest_palindrome("ene"))  # ene
    print(largest_palindrome("ene"))  # ene
    print(largest_palindrome("Was it a car or a cat I saw"))  # ene
    print(largest_palindrome("Murder for a jar of red rum"))  # ene
    print(largest_palindrome("Go hang a salami, I'm a lasagna hog"))  # ene
    print(largest_palindrome("Rats live on no evil star"))  # ene
    # ive on time, emit no evil
    print(largest_palindrome("live on time emit no evil"))
    print(largest_palindrome("step on no pets"))  # step on no pets
    print(largest_palindrome("      "))  # spaces

    # print(largest_palindrome(123124)) #None
    print(largest_palindrome(123321))  # 123321
    print(largest_palindrome(123.321))  # 123321

    print(largest_palindrome(True))  # None
    print(largest_palindrome(False))  # None
    # print(largest_palindrome(02)) # None
    # future implementation, see if the number is palidrome

    # class New:
    #     pass
    # print(largest_palindrome(New())) # None

    # x = lambda a : a + 10
    # print(largest_palindrome(x)) # None
