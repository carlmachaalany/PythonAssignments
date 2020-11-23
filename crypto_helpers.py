# Name: Carl Machaalani
# ID: 260895058
# A program that creates some helper functions for the cipher program

# Assign a variable to all the letters in the English alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def in_engl_alpha(string):
    
    """ (str) --> bool

    This function checks if the input string
    (string) is a non-empty string containing
    only characters from the English alphabet.

    >>> in_engl_alpha("e")
    True
    >>> in_engl_alpha("O")
    True
    >>> in_engl_alpha("squirrels")
    True
    >>> in_engl_alpha("squirrels and beavers")
    False
    >>> in_engl_alpha("squIrrelsaNdbeaVers")
    True
    >>> in_engl_alpha("*")
    False
    >>> in_engl_alpha("é")
    False
    >>> in_engl_alpha("")
    False
    >>> in_engl_alpha(" ")
    False
    """
    
    # if the string is an empty string, return False
    if len(string) == 0:
        return False
    
    # changing all upper case letters to lower case
    string = string.lower()
    
    # iterate through the string 
    for char in string:
        
        # if the character is from the english alphabet 
        if char in ALPHABET:
            # pass to the next character
            continue
        
        # if the character is not from the english alphabet or is a space
        else:
            # return False and end execution of the function
            return False
        
    # return True if all characters in the string are from the english alphabet
    return True

def shift_char(char, n):
    
    """ (str, int) --> str

    This function takes a string char containing one
    of the letters of the English alphabet and an
    integer n and returns the lower case letter
    which appears n position later in the alphabet.
    If the string is not a letter in the English
    alphabet, the function returns the string itself.

    >>> shift_char('t',4)
    'x'
    >>> shift_char('y',3)
    'b'
    >>> shift_char('B',-3)
    'y'
    >>> shift_char('*',3)
    '*'
    >>> shift_char('g',86)
    'o'
    >>> shift_char('dog',5)
    Traceback (most recent call last):
    ValueError: the input string should contain a single character
    >>> shift_char('',4)
    Traceback (most recent call last):
    ValueError: the input string should contain a single character
    >>> shift_char(' ',4)
    ' '
    >>> shift_char("z",26)
    'z'
    >>> shift_char('a',-53)
    'z'
    """
    
    # if the string recieved is not a single character
    if len(char) != 1:
        # raise a Value error
        raise ValueError("the input string should contain a single character")
    
    # changing the character to lower case in case it is upper case
    char = char.lower()
    
    # if the character is a letter in the English alphabet
    if in_engl_alpha(char):
        
        # iterate through the letters of the English alphabet
        for i in range(len(ALPHABET)):
            
            # if the character is the same as that in positon i in ALPHABET
            if char == ALPHABET[i]:
                # We reassign the index to the index n position later in the alphabet
                i += n
                
                # iterate as long as the index is out of range
                while i>25 or i<-26:
                    # if the index is too big
                    if i>25:
                        # subtract 26 in order to reach the new position
                        i -= 26
                    # if the index is too small
                    else:
                        # add 26 in order to reach the new position
                        i+= 26
                    
                # return the new character
                return ALPHABET[i]
            
    # return the same character if it is not a letter in the English alphabet
    return char

def get_keys(string):
    
    """ (str) --> list

    This function takes a string as input and
    returns a list containing the positions of
    each character in the string as a letter of
    the English alphabet. The function raises
    an error if one of the characters is not
    from the English alphabet.

    >>> get_keys("squirrel")
    [18, 16, 20, 8, 17, 17, 4, 11]
    >>> get_keys("sQuiRreL")
    [18, 16, 20, 8, 17, 17, 4, 11]
    >>> get_keys("")
    []
    >>> get_keys("d0gs")
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet
    >>> get_keys(" ")
    Traceback (most recent call last):
    ValueError: the input string must contain only characters from the English alphabet
    """
    
    # changing all upper case letters to lower case
    string = string.lower()
    
    # create a new empty list in which we will add the keys to
    list_of_keys = []
    
    # iterate through the characters of the string
    # Note if the string is empty, python will not enter this loop
    for char in string:
        
        # if the character is not from the English alphabet, raise a Value Error
        if not in_engl_alpha(char):
            raise ValueError("the input string must contain only characters from the English alphabet")
        
        # iterate through the letters of the English alphabet
        for i in range(len(ALPHABET)):
            # if the character is the same as that in positon i in ALPHABET 
            if char == ALPHABET[i]:
                # add the index i to the list 
                list_of_keys.append(i)
                # In order to be more efficient, we stop iterating when we find the index
                break
            
    # return the list of indeces
    return list_of_keys

def pad_keyword(string,n):
    
    """ (str,int) --> str

    This function takes a string and an
    integer as input and returns a string
    of length n containing concatenated
    characters of the input string. If the
    input string is empty, the function
    raises a value error.

    >>> pad_keyword("dogs",10)
    'dogsdogsdo'
    >>> pad_keyword("squirrel",4)
    'squi'
    >>> pad_keyword("c a t",5)
    'c a t'
    >>> pad_keyword("d*Gs",6)
    'd*Gsd*'
    >>> pad_keyword("",5)
    Traceback (most recent call last):
    ValueError: the input string must contain at least one character
    """
    
    # if the input string is empty
    if len(string)==0:
        # raise a Value Error
        raise ValueError("the input string must contain at least one character")
    
    # Assign a variable containing an empty string, in which we will
    # add characters to, to result in the string we should then return
    goal_string = ""
    
    # Assign a variable storing the index of string
    # we've reached as we are adding characters to goal_string
    string_index = 0
    
    # Iterate as long as the length of
    # goal_string is less than the goal number n
    while len(goal_string) < n:
        
        # To goal_string, add the character at index string_index of string
        goal_string += string[string_index]
        
        # If the index after the current string_index is out of range, that
        # means the string ended and we rezero string_index to start again. 
        if string_index + 1 == len(string):
            string_index = 0
            
        # If the string has not finished yet, we go to the next character
        else:
            string_index += 1
    
    # return goal_string when all necessary characters are added
    return goal_string
            
    
    