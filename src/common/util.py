''' common infrastructure that helps the logic of the api '''


def largest_palindrome(phrase):
    ''' Is a function to find the largest palindrome from the string,
    the rules for finding this type of sub string is:
     - Acá los espacios son considerados al igual que las mayúsculas y minúsculas.
     - Los espacios en blanco no se eliminan.
     - Se diferencia entre mayúsculas y minúsculas.
     - No se reemplazan caracteres en las cadenas
    return: the largest palindrome and if it is two, it returns the first answear
    '''
    # if is not a string and it is a number, pass to string and see if the
    # number is palidrome
    if type(phrase) in (int, float):
        phrase = str(phrase)

    if not type(phrase) is str or len(phrase) == 0:
        return None

    # for letter in range(len(phrase), 1):
    #     # pass
    #     print(phrase[letter + 1] == phrase[letter + 1])

    # count in reverse, delete the extra number of leght, and start to 0
    for i in range(len(phrase) - 1, -1, -1):
        # print(i)
        print(phrase[i])

    return phrase


if __name__ == '__main__':
    """
    This is for making quick testing of the function
    """
    print(largest_palindrome("new"))  # None
    print(largest_palindrome("kayak"))  # None
    print(largest_palindrome("abba"))  # abba
    # print(largest_palindrome("a"))  # a
    # print(largest_palindrome("abcc"))  # cc
    # print(largest_palindrome("Anita lava la tina"))  # ava
    # print(largest_palindrome("12345654321"))  # 12345654321
    # print(largest_palindrome("abaaaa"))  # aba
    # print(largest_palindrome("n "))  # n_
    # print(largest_palindrome("perl lrep"))  # perl lrep
    # print(largest_palindrome("abcda"))  # abcda
    # print(largest_palindrome("n n"))  # n n
    # print(largest_palindrome("U+006- U+01"))  # 00
    # print(largest_palindrome("/@[#-;!;$#Q"))  # ;!;
    # print(largest_palindrome("d     sadas       ie"))  # space sadas space
    # print(largest_palindrome("1-2-3-4 4-3-2-1"))  # 1-2-3-4 4-3-2-1
    # print(largest_palindrome("passion"))  # ss
    # print(largest_palindrome(None))  # None
    # print(largest_palindrome("three"))  # ee
    # print(largest_palindrome("tw"))  # tw
    # print(largest_palindrome("éné"))  # éné
    # print(largest_palindrome("ene"))  # ene
    # print(largest_palindrome("ene"))  # ene
    # print(largest_palindrome("Was it a car or a cat I saw"))  # ene
    # print(largest_palindrome("Murder for a jar of red rum"))  # ene
    # print(largest_palindrome("Go hang a salami, I'm a lasagna hog"))  # ene
    # print(largest_palindrome("Rats live on no evil star"))  # ene
    # print(largest_palindrome("Live on time, emit no evil"))  # ene
    # print(largest_palindrome("Step on no pets"))  # ene

    # # future implementation, see if the number is palidrome
    # # print(largest_palindrome(123124)) #None
    # print(largest_palindrome(123321))  # 123321
    # print(largest_palindrome(123.321))  # 123321

    # print(largest_palindrome(True))  # None
    # print(largest_palindrome(False))  # None
    # # print(largest_palindrome(02)) # None

    # # class New:
    # #     pass
    # # print(largest_palindrome(New())) # None

    # # x = lambda a : a + 10
    # # print(largest_palindrome(x)) # None
