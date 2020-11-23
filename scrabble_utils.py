# Name: Carl Machaalani
# ID: 260895058

# A module that contains several functions needed to 
# implement the general mechanics of a game of scrabble

# import random module
import random

# import everything from board_utils module
from board_utils import *

# import everything from dicts_utils module
from dicts_utils import *


def display_rack(r):
    
    """ (dict) -> NoneType
    
    This function takes the rack of the player as input
    and displays the letters that are are on the rack
    using upper case.

    >>> display_rack({'a': 2, 'f': 1, 'g': 2, 'o': 1, 'z': 1})
    A A F G G O Z 
    >>> display_rack({'h': 2, 'o': 1, 'm': 2, 'e': 1, ' ': 1})
    H H O M M E   
    >>> display_rack({'': 2, 'o': 1, 'm': 2, 'e': 1, ' ': 1})
      O M M E   
    >>> display_rack({'Z': 2, 'y': 3, 'k': 0})
    Z Z Y Y Y 
    
    """
    
    # iterate through the characters of the rack
    for c in r:
        
        # iterate as many times as the value of each character
        for i in range(r[c]):
            
            # display the character (upper case) on the same line
            print(c.upper(), end = " ")
            
def has_letters(r, word):
    
    """ (dict, str) -> bool

    This function takes the rack and a word as input. If
    the characters in the string are available in the rack,
    the function returns True and removes the letters of
    the word from the rack. Otherwise, it returns False.
    
    >>> r = {'a': 2, 'c': 1, 't': 1, 'i': 2, 'r': 1}
    >>> has_letters(r, 'cat')
    True
    >>> r == {'a': 1, 'i': 2, 'r': 1}
    True
    >>> r = {'b': 4, 'c': 2, 't': 5}
    >>> has_letters(r, 'bat')
    False
    >>> r == {'b': 4, 'c': 2, 't': 5}
    True
    >>> r = {'z': 1, 'e':1, 'b':1, 'r':1, 'a':1}
    >>> has_letters(r, 'zebra')
    True
    >>> r == {}
    True
    >>> r = {'Z': 1, 'e':1, 'b':1, 'r':1, 'a':1}
    >>> has_letters(r, 'zebra')
    False
    >>> r == {'Z': 1, 'e':1, 'b':1, 'r':1, 'a':1}
    True
    
    """
    
    # Create a variable word_dic storing the input word as a dictionary where the
    # keys are the characters and their values are their number of occurences
    word_dic = count_occurrences(word)
    
    # subtract the dictionary word_dic from the input dictionary
    # r and return True if it works, false otherwise
    return subtract_dicts(r, word_dic)

# this function is a helper function for the function refill_rack
def count_letters(dic):
    
    """ (dict) --> int

    This function takes as input a dictionary where the keys represent
    letters in a rack and their values represent the letter's frequency
    in the rack. The function returns the number of letters in the rack.
    
    >>> r = {'e': 3, 'q' : 1, 'r' : 1}
    >>> count_letters(r)
    5
    >>> r = {'a': 2, 'b': -1, 'c': 5}
    >>> count_letters(r)
    6
    >>> r = {'g': -4, 'b': 0, 'c': 1}
    >>> count_letters(r)
    -3
    
    """
    
    # Create variable summation and set to 0
    summation = 0
    
    # iterate through the keys of the dictionary
    for key in dic:
        # add the value of the key to the summation
        summation += dic[key]
    
    # return summation
    return summation
        
def refill_rack(r, pool, n):
    
    """ (dict, dict, int) -> NoneType

    This function takes the rack, the pool of letters, and an
    integer n as input. It then fills the rack by picking
    letters randomly from the pool until either the rack has
    n letters or the pool gets empty.
    
    >>> random.seed(5)
    >>> r1 = {'a': 2, 'k': 1}
    >>> b = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'z': 1}
    >>> refill_rack(r1, b, 7)
    >>> r1
    {'a': 2, 'k': 1, 's': 1, 'l': 1, 't': 1, 'n': 1}
    >>> b
    {'a': 1, 'e': 2, 'h': 1, 'l': 1, 'p': 2, 's': 2, 't': 1, 'z': 1}
    >>> random.seed(1)
    >>> r1 = {'b': 2, 'l': 1}
    >>> pool = {'a': 4, 'b': 3, 'c': 2, 'f': 1, 'z': 1, 'l': 2, 'p': 1}
    >>> refill_rack(r1, pool, 9)
    >>> r1
    {'b': 3, 'l': 2, 'a': 3, 'z': 1}
    >>> pool
    {'a': 1, 'b': 2, 'c': 2, 'f': 1, 'l': 1, 'p': 1}
    >>> random.seed(3)
    >>> r1 = {'c': 3, 'l': 1}
    >>> pool = {'a': 1, 'h': 2, 'g': 1}
    >>> refill_rack(r1, pool, 11)
    >>> r1
    {'c': 3, 'l': 1, 'h': 2, 'g': 1, 'a': 1}
    >>> pool
    {}
    >>> r1 = {}
    >>> pool = {'a': 2, 'y': 4}
    >>> refill_rack(r1, pool, 5)
    >>> r1
    {'y': 3, 'a': 2}
    >>> pool
    {'y': 1}
    
    """
    
    # create a variable storing a list of the pool letters
    pool_list = flatten_dict(pool)
    
    # keep iterating while there are less than n letters in the rack
    # and there are still letters in the pool
    while count_letters(r)<n and len(pool_list)>0:
        
        # draw a letter from the pool 
        random_letter = random.choice(pool_list)
        
        # add the letter to the rack
        r[random_letter] = r.get(random_letter, 0) + 1
         
        # remove the letter from the list of the pool
        pool_list.remove(random_letter)
        
        # subtract one from the letter's value in the dictionary pool
        pool[random_letter] -= 1
        # if the letter's value becomes 0, delete it from the dictionary pool
        if pool[random_letter] == 0:
            del pool[random_letter]
            
def compute_score(list_of_str, dict_letters_pts, dict_valid_words):
    
    """ (list, dict, dict) -> int
    
    This function takes a list of words, a dictionary representing
    the points of each letter, and a dictionary representing valid
    words as input. The function returns the total score obtained
    by the list of words. If any of the words is not valid, the
    function returns 0.
    
    >>> v = {'a': 1, 'l': 3, 'b': 2, 't': 4}
    >>> w = ['bat', 'van', 'welcome', 'to', 'confusion', 'wild', 'go', 'science', 'bowl', 'wing']
    >>> d = create_scrabble_dict(w)
    >>> compute_score(['bat'], v, d)
    7
    >>> compute_score(['zero'], v, d)
    0
    >>> compute_score(['back'], v, d)
    0
    >>> compute_score(['wing'], v, d)
    0
    
    """
    
    # Create a variable score and set to 0
    total_score = 0
    
    # iterate through the words of the list of strings
    for word in list_of_str:
        
        # if the word is not valid, return 0 and end execution
        if not is_valid_word(word, dict_valid_words):
            return 0
        
        # add the score of the word to the total score
        total_score += get_word_score(word, dict_letters_pts)
    
    # return total score
    return total_score
           
def place_tiles(board, letters, row, col, direction):
    
    """ (list, str, int, int, str) -> list
    
    This function takes a 2D list representing the board, the letters
    the player wants to add, the row, the column, and the direction as
    input. The function modifies the board after adding the letters
    accordingly and returns a list of words created by adding
    those letters to the board.

    >>> b = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(b, 'back', 1, 0, 'right')
    ['back']
    >>> b
    [[' ', ' ', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(b, 'bt', 0, 1, 'down')
    ['bat']
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> place_tiles(b, 'ap', 2, 2, 'right')
    ['ca', 'kp', 'tap']
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', 'a', 'p'], [' ', ' ', ' ', ' ']]
    >>> place_tiles(b, 'sr', 0, 2, 'down')
    ['bs', 'scar']
    >>> b
    [[' ', 'b', 's', ' '], ['b', 'a', 'c', 'k'], [' ', 't', 'a', 'p'], [' ', ' ', 'r', ' ']]
    
    """
    
    # Create a new empty list in which we will add the words created
    new_words = []
    
    
    # if the direction is right
    if direction == 'right':
        
        # Save the input column in a variable since we're gonna use it after
        input_col = col
        
        # extract the row on which we are adding the letters
        complete_row = board[row]
        
        # Set the letters added so far and the index of letters to 0
        letters_added = i = 0
        
        # keep iterating unitl we've added all the letters
        while letters_added < len(letters):
            
            # Assign a variable to the square we are looking to add the letter to
            square = complete_row[col]
            
            # if the square is empty
            if square == " ":
                
                # FIRST: We add the letter to the board
                
                # add the letter at index i of letters to the square
                complete_row[col] = letters[i]
                
                # add 1 to the number of letters added and move to the next letter in letters
                letters_added += 1
                i += 1
                
                
                # SECOND: We add the hook word to the list new_words
                
                # extract the column to which we added the letter
                complete_col = get_vertical_axis(board, col)
                
                # extract the vertical hook word from this column 
                hook_word = find_word(complete_col, row)
                
                # add the hook word to the list new_words only if its length > 1
                if len(hook_word)>1:
                    new_words.append(hook_word)
            
            
            # move to the next column after each iteration
            col += 1
        
        
        # THIRD: We add the main word to the list new_words
        
        # extract the horizontal main word and add it to new_words
        main_word = find_word(board[row], input_col)
        new_words.append(main_word)
    
    
    # if the direction is down
    elif direction == 'down':
        
        # Save the input row in a variable since we're gonna use it after
        input_row = row
        
        # Set the letters added so far and the index of the letters to 0
        letters_added = i = 0
        
        # keep iterating unitl we've added all the letters
        while letters_added<len(letters):
            
            # Assign a variable to the square we are looking to add the letter to
            square = board[row][col]
            
            # if the square is empty
            if square == " ":
                
                # FIRST: We add the letter to the board
                
                # add the letter at index i of letters to the square
                board[row][col] = letters[i]
                
                # add 1 to the number of letters added and move to the next letter in letters
                letters_added += 1
                i += 1
                
                
                # SECOND: We add the hook word to the list new_words
                
                # extract the row to which we added the letter
                complete_row = board[row]
                
                # extract the horizontal hook word from this row
                hook_word = find_word(complete_row, col)
                
                # add the hook word to the list new_words only if its length > 1
                if len(hook_word)>1:
                    new_words.append(hook_word)
            
            
            # move to the next row after each iteration
            row += 1
        
        
        # THIRD: We add the main word to the list new_words
        
        # extract the column in which we added the main word
        complete_col = get_vertical_axis(board, col)
        
        # extract the main word and add it to new_words
        main_word = find_word(complete_col , input_row)
        new_words.append(main_word)       
    
    
    # finally, return the list new_words
    return new_words
        
def make_a_move(board, r, letters, row, col, direction):
    
    """ (list, dict, str, int, int, str) -> list

    This function takes the board, the rack, the letter the player
    want to placee, the row, the column, and the direction as input.
    The function then makes the move on the board and returns a list
    of words created by performing the move. If the move, is not valid,
    an error is raised.
    
    >>> b = [[' ', ' ', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> r = {'b': 2, 'a': 1, 'r' : 2, 't' : 1, 'p':1}
    >>> make_a_move(b, r, 'bt', 0, 1, 'down')
    ['bat']
    >>> r == {'b': 1, 'a': 1, 'r' : 2, 'p':1}
    True
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> words = make_a_move(b, r, 'ap', 2, 2, 'right')
    >>> words.sort()
    >>> words
    ['ca', 'kp', 'tap']
    >>> r == {'b': 1, 'r' : 2}
    True
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', 'a', 'p'], [' ', ' ', ' ', ' ']]
    >>> r = {'b': 1, 'r' : 2, 'a': 2}
    >>> make_a_move(b, r, 'bar', 3, 0, 'Right')
    []
    >>> r == {'b': 1, 'r' : 2, 'a': 2}
    True
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', 'a', 'p'], [' ', ' ', ' ', ' ']]
    >>> make_a_move(b, r, 'bar', 3, 2, 'right')
    Traceback (most recent call last):
    IndexError: Not enough space on the board
    >>> r == {'b': 1, 'r' : 2, 'a': 2}
    True
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', 'a', 'p'], [' ', ' ', ' ', ' ']]
    >>> make_a_move(b, r, 'bag', 3, 0, 'right')
    Traceback (most recent call last):
    ValueError: Those letters are not available on the rack
    >>> r == {'b': 1, 'r' : 2, 'a': 2}
    True
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', 'a', 'p'], [' ', ' ', ' ', ' ']]
    >>> make_a_move(b, r, 'baggage', 3, 2, 'right')
    Traceback (most recent call last):
    IndexError: Not enough space on the board
    >>> r == {'b': 1, 'r' : 2, 'a': 2}
    True
    >>> b
    [[' ', 'b', ' ', ' '], ['b', 'a', 'c', 'k'], [' ', 't', 'a', 'p'], [' ', ' ', ' ', ' ']]
    
    """
    
    # if the direction is neither right or down
    if direction not in ['right', 'down']:
        #return an empty list
        return []
    
    # if the direction is to the right
    if direction == 'right':
        # extract the row on which we will add the letters
        complete_row = board[row]
        # check if the letters fit on the board and assign the boolean value to a variable is_fit
        is_fit = fit_on_board(complete_row, letters, col)
        
    # if the direction is down
    else:
        # extract the column on which we will add the letters
        complete_col = get_vertical_axis(board, col)
        # check if the letters fit on the board and assign the boolean value to a variable is_fit
        is_fit = fit_on_board(complete_col, letters, row)
    
    # if the letters do not fit on the board as specified, raise an IndexError
    if not is_fit:
        raise IndexError("Not enough space on the board")
    
    # if the letters are not available on the rack, raise a ValueError
    # if the letters are available, remove the letters from the rack
    if not has_letters(r, letters):
        raise ValueError("Those letters are not available on the rack")
    
    # place the letters on the board as specified and return the list of new words created
    return place_tiles(board, letters, row, col, direction)
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    


    
    
    
    
    
        