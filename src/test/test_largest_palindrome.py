#!/usr/bin/env python3
''' This is for testing the app '''
# from  .common.util import largest_palindrome
from src.common.util import *
# from palindrome-api.src.common.util import largest_palindrome

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
