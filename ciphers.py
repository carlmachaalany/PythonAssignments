# Name: Carl Machaalani
# ID: 260895058
# A program that encrypts/decrypts Caesar's cipher and Vigenere's cipher

# import all helper functions and variables from crypto_helpers
from crypto_helpers import *

def caesar(message,k,m):
    
    """ (str,int,int) --> str

    This function takes the message to encrypt/decrypt,
    an integer k which is the key of the cipher, and
    an integer m as input. If m=1, the message will be
    encrypted, and if m=-1, the message will be decrypted.
    Otherwise, a Value error is raised. The function then
    returns the encrypted/decrypted message using Caesar's
    cipher.

    >>> ceasar("efg",5,1)
    'jkl'
    >>> ceasar("wtaad",15,-1)
    'hello'
    >>> ceasar("hello",15,1)
    'wtaad'
    >>> ceasar("G jmtc Amkn 202",2,1)
    'i love comp 202'
    >>> ceasar("G jmtc Amkn 202",-2,-1)
    'i love comp 202'
    >>> ceasar("",3,-1)
    ''
    >>> ceasar(" ",5,1)
    ' '
    >>> ceasar("squirrel",5,11)
    Traceback (most recent call last):
    ValueError: mode not supported
    """
    
    # if the last input integer is not 1 or -1, raise a Value error
    if m not in [-1,1]:
        raise ValueError("mode not supported")
    
    # Assign a variable containing an empty string, in which we will
    # add characters to, to result in the encrypted/decrypted message 
    goal_message = ""
    
    # if m is 1, we encrypt
    if m==1:
        # iterate through the characters of the message
        for char in message:
            # move the character by k positions and add resulting character to goal_message
            goal_message += shift_char(char,k)
    
    # if m is -1, we decrypt
    else:
        # iterate through the characters of the message
        for char in message:
            # move the character by -k positions and add resulting character to goal_message
            goal_message += shift_char(char,-k)
            
    # return goal_message when all necessary characters are added
    return goal_message

def vigenere(message, key, m):
    
    """ (str, str, int) --> str

    This function takes as input the message to
    encrypt/decrypt, the key word key of the cipher,
    and an integer m representing the mode
    (encrypt or decrypt). If m=1, the message will
    be encrypted, and if m=-1, the message will be
    decrypted. Otherwise, a Value error is raised.
    The function then returns the encrypted/decrypted
    message using Vigenere's cipher.

    >>> vigenere('squirrel','cat',1)
    'uqnkrkgl'
    >>> vigenere('uqnkrkgl','cat',-1)
    'squirrel'
    >>> vigenere('beaver','i love comp',-1)
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet
    >>> vigenere('i love comp','beaver',-1)
    'h ltrn yorl'
    >>> vigenere('i love comp','DOGSSS',1)
    'l rgnw queh'
    >>> vigenere('fine','hot',7)
    Traceback (most recent call last):
    ValueError: mode not supported
    >>> vigenere('fine','h0t',1)
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet
    >>> vigenere('beaver','',1)
    Traceback (most recent call last):
    ValueError: the input string must contain at least one character
    """
    
    # if the last input integer is not 1 or -1, raise a Value error
    if m not in [-1,1]:
        raise ValueError("mode not supported")
    
    # Assign a variable to an empty string, in which we
    # will add characters to, to result in the encrypted string
    goal_message = ""
    
    # Assign a variable to a string of same length as the message
    # containing concatenated characters of the input key.
    # If the key is an empty string, a Value error is raised here
    keyword_sequence = pad_keyword(key, len(message))
    
    # Assign a variable to a list of integers representing the position
    # (in the English alphabet) of each character in the key word sequence
    # If one of the characters is not from the english alphabet, a Value Error is raised here
    list_of_indeces = get_keys(keyword_sequence)
    
    # if m is 1, we encrypt 
    if m==1:
        # iterate through the characters of the message
        for i in range(len(message)):
            # shift each character to its corresponding encrypted position 
            goal_character = shift_char(message[i],list_of_indeces[i])
            # add resulting character to the goal message
            goal_message += goal_character
    
    # if m is -1, we decrypt
    else:
        # iterate through the characters of the message
        for i in range(len(message)):
            # shift each character to its corresponding decrypted position
            goal_character = shift_char(message[i],-list_of_indeces[i])
            # add resulting character to the goal message
            goal_message += goal_character
            
    # return goal_message when all necessary characters are added 
    return goal_message


    

    
    
            
    
        
        
    
    


