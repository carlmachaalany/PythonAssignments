# Name: Carl Machaalani
# ID: 260895058

# A module that contains several helper functions 
# needed to implement a part of scrabble.

def count_occurrences(string):
    
    """ (str) -> dict

    This function takes a string as input and returns
    a dictionary where the keys are the characters in
    the string and the values are their corresponding
    number of occurences in the string.
    
    >>> d = count_occurrences('mama')
    >>> d == {'m':2, 'a':2}
    True
    >>> d = count_occurrences('')
    >>> d == {}
    True
    >>> d = count_occurrences('mississipi')
    >>> d == {'m':1, 'i':4, 's':4,'p':1}
    True
    >>> d = count_occurrences("you're")
    >>> d == {'y':1, 'o':1, 'u':1, "'":1, 'r':1, 'e':1}
    True
    
    """
    
    # Create an empty dictionary
    dic = {}
    
    # iterate though the characters of the string
    for char in string:
        
        # if the chararacter is in the dictionary, add 1 to its value
        # if the character is not in the dictionary, add it and set its value to 1 
        dic[char] = dic.get(char, 0) + 1
         
    # return the dictionary
    return dic

def flatten_dict(dic):
    
    """ (dict) -> list

    This function takes a dictionary as an input where all
    the values are non-negative integers. It returns a list
    containing the keys in the dictionary where each key
    appears in the list as many times as their values.
    
    >>> d = {'a' : 2, 'f' : 1, 'k' : 5}
    >>> lis = flatten_dict(d)
    >>> lis.count('a')
    2
    >>> lis.count('f')
    1
    >>> lis.count('k')
    5
    >>> lis.sort()
    >>> lis
    ['a', 'a', 'f', 'k', 'k', 'k', 'k', 'k']
    >>> d = {'comp' : 1, 'is' : 1, 'so' : 5, 'cool':1}
    >>> lis = flatten_dict(d)
    >>> lis.sort()
    >>> lis
    ['comp', 'cool', 'is', 'so', 'so', 'so', 'so', 'so']
    >>> d = {'a': 0}
    >>> lis = flatten_dict(d)
    >>> lis.sort()
    >>> lis
    []
    >>> d = {'a': 0, 'b':1}
    >>> lis = flatten_dict(d)
    >>> lis.sort()
    >>> lis
    ['b']
    >>> d = {}
    >>> lis = flatten_dict(d)
    >>> lis.sort()
    >>> lis
    []
    
    """
    
    # Create a new list
    returned_list = []
    
    # iterate through the keys of the input dictionary
    for key in dic:
        
        # iterate as many times as the value associated to the key
        for i in range(dic[key]):
            # append the key to the new list
            returned_list.append(key)
            
    # return the list
    return returned_list

def get_word_score(word, dic):
    
    """ (str, dict) -> int

    This function takes as input a string and a dictionary mapping characters
    to integer representing the number of points each character is worth. The
    function returns the total score of the word. If a given character is not
    a key in the dictionary, the character is considered to have a value of 0.
    
    >>> v = {'a': 2, 'r': 3, 'f': -1, 'b': 1}
    >>> get_word_score('dog', v)
    0
    >>> get_word_score('rat', v)
    5
    >>> get_word_score('fool', v)
    -1
    >>> v = {}
    >>> get_word_score('banana', v)
    0
    
    """
    
    # Create a variable score and set to 0 
    score = 0
    
    # iterate through the characters of the word
    for char in word:
        
        # for every character of the word, iterate through 
        # the dictionary to find the same character. 
        for letter in dic:
            
            # if the character is found, add its score.
            # if not, nothing is added to the score rendering the value of the character to be 0
            if letter == char:
                score += dic[letter]
                
    # return the score at the end
    return score

def is_subset(mini_d, big_d):
    
    """ (dict, dict) -> bool
    
    This function takes two dictionaries mini_d and big_d
    as input and returns True if mini_d is a subset of
    big_d, false otherwise.

    >>> a = {'d': 3, 'e':1}
    >>> b = {'d': 3, 'e':2, 'f': 0}
    >>> c = {'d': 4, 'e':1}
    >>> d = {'d': 4, 'e':1}
    >>> is_subset(a, b)
    True
    >>> is_subset(b, a)
    False
    >>> is_subset(a, c)
    True
    >>> is_subset(c, b)
    False
    >>> is_subset(c, d)
    True
    
    """
    
    # iterate through the keys of the dictionary we are checking whether it is a subset or not
    for key in mini_d:
        
        # if the key is not in the other dictionary, return False directly without even checking the second condition
        # if the key is in the other dictionary, return False if its value in mini_d is greater than than in big_d
        if key not in big_d or mini_d[key]>big_d[key]:
            return False
    
    # return True if the function survives till this line of code 
    return True

def subtract_dicts(d1, d2):
    
    """ (dict, dict) -> bool

    This function takes two dictionaries d1 and d2 where all the values
    are non-negative as input. If d2 is a subset of d1, the function
    updates d1 by replacing the values associated to the common keys
    with the difference between the original value in d1 and the value
    in d2 and returns True. Otherwise, d1 remains as is and the function
    returns False.
    
    >>> a = {'d': 3, 'e':1}
    >>> b = {'d': 3, 'e':2, 'f': 5}
    >>> c = {'d': 4, 'e':1}
    >>> d = {'d': 4, 'e':1}
    >>> subtract_dicts(a, b)
    False
    >>> a == {'d': 3, 'e':1}
    True
    >>> subtract_dicts(c, b)
    False
    >>> c == {'d': 4, 'e':1}
    True
    >>> subtract_dicts(b, a)
    True
    >>> b == {'e':1, 'f': 5}
    True
    >>> subtract_dicts(c, d)
    True
    >>> c == {}
    True

    """
    
    # if d2 is a subset of d1
    if is_subset(d2, d1):
        
        # iterate through the keys of d2
        for key in d2:
            
            # subtract the value of the key in d2 from that in d1
            d1[key] -= d2[key]
            
            # if the new value of the key is 0, delete the item
            if d1[key] == 0:
                del d1[key]
     
        # return True after the whole modification is done
        return True
    
    # return False if d2 is not a subset of d1 
    return False

def create_scrabble_dict(lis):
    
    """ (list) -> dict

    This function takes a list of strings as input. It returns a dictionary
    that maps integers representing the number of characters in a word to a
    dictionary of words with the specified length. The latter maps a single
    letter to a list of words beginning with such letter.
    
    >>> w = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = create_scrabble_dict(w)
    >>> d == {2 : {'a': ['aa'], 'q': ['qi'], 'z': ['za']}, 3 : {'c': ['cat', 'can', 'cow'], \
      'd': ['dog', 'dad']}, 5 : {'h': ['hippo'], 'u' : ['umami', 'uncle'] }}
    True
    >>> w = [' ', 'cat', '"', 'and', 'dogs', 'squirrels', 'map', 'cop']
    >>> d = create_scrabble_dict(w)
    >>> d == {1 : {' ': [' '],'"': ['"']}, 3 : {'c': ['cat','cop'], 'a': ['and'], \
        'm': ['map']},4 : {'d': ['dogs']}, 9: {'s': ['squirrels']}}
    True
    >>> w = [' ']
    >>> d = create_scrabble_dict(w)
    >>> d == {1: {' ': [' ']}}
    True
    >>> w = ['']
    >>> d = create_scrabble_dict(w)
    Traceback (most recent call last):
    IndexError: string index out of range
    
    """
    
    # Create a new empty dictionary
    d = {}
    
    # iterate thorugh the strings of the list
    for string in lis:
        
        # Create a variable storing the number of characters in the string
        num_of_char = len(string)
        
        # Create a variable storing the first character of the string
        first_char = string[0]
        
        # if the number of characters of the string is already a key in the new dictionary d
        if num_of_char in d:
            
            # if the first character of the string is a key in the dictionary mapped by num_of_char
            if first_char in d[num_of_char]:
                # append the string to the list mapped by the first character of the string
                d[num_of_char][first_char].append(string)
                
            # if the first character of the string is not a key in the dictionary mapped by num_of_char 
            else:
                # create a new key representing the first character mapping to a list containing the string
                d[num_of_char][first_char] = [string]
        
        # if the number of characters of the string is not a key in the new dictionary d
        else:
            # create a new key in d representing the number of characters mapping to dictionary
            # containing a key representing the first character mapping to a list containing the string
            d[num_of_char] = {first_char: [string]}
    
    # return the dictionary at the end
    return d

def is_valid_word(word, dic):
    
    """ (str, dict) -> bool

    This function takes a word and a dictionary as input.
    The function returns True if the input word string
    appears in the dictionary, false otherwise.

    >>> w = ['ae','aa', 'me', 'cat', 'can', 'map', 'dog', 'cop', 'squirrel', 'tsunami', 'aunt']
    >>> d = create_scrabble_dict(w)
    >>> is_valid_word('map', d)
    True
    >>> is_valid_word('aa', d)
    True
    >>> is_valid_word('', d)
    False
    >>> is_valid_word(' ', d)
    False
    >>> is_valid_word('tom', d)
    False
    >>> is_valid_word('Cat', d)
    False
    
    """
    
    # iterate through the keys in dic
    for num_of_char in dic:
        
        # iterate through the keys of the value dictionary of the key
        for first_char in dic[num_of_char]:
            
            # iterate through the strings in the list mapped by the first character
            for string in dic[num_of_char][first_char]:
                
                # if the word was found to be in one of the lists, return True
                if string == word:
                    return True
                
    # if the word was not found in the dictionary, return False
    return False


            
        