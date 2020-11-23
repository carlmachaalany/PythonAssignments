# Name: Carl Machaalani
# ID: 260895058

# A module that contains several helper functions needed
# to implement a srabble board.

def create_board(rows, cols):
    
    """ (int, int) -> list
    
    This function takes the number of rows and columns as
    input and returns an empty board of scrabble in the form
    of a 2D list of strings where all the elements of the
    sublists are strings containing only the space character.
    
    >>> create_board(3,4)
    [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    >>> create_board(1,1)
    [[' ']]
    >>> create_board(0,3)
    Traceback (most recent call last):
    ValueError: Inputs must be positive
    >>> create_board(-1,3)
    Traceback (most recent call last):
    ValueError: Inputs must be positive
    
    """
    
    # raise a ValueError if either of the inputs is negative
    if rows<=0 or cols <=0:
        raise ValueError("Inputs must be positive")
    
    # Create an empty list in which we will form the 2D list 
    board = []
    
    # iterate number of row times
    for i in range(rows):
        
        # Create an empty list
        mini_list = []
        
        # iterate number of column times
        for j in range(cols):
            # append at each iteration a space character to the mini list
            mini_list.append(" ")
            
        # append the resulting mini_list to the big list    
        board.append(mini_list)
        
    # return the big 2D list
    return board

def display_board(board):
    
    """ (list) -> NoneType
    
    This function takes a two dimensional list of strings as input
    representing a board. The function then displays the board, one
    row per line.
    
    >>> b = [[' ', ' ', ' ', ' ', ' '], [' ', 'c', 'a', 't', 's']]
    >>> display_board(b)
        0   1   2   3   4
      +-------------------+
    0 |   |   |   |   |   |
      +-------------------+
    1 |   | c | a | t | s |
      +-------------------+
    >>> b = [['I',' ',' ',' '],['l','o','v','e'],['C','O','M','P'],['2','0','2',' ']]
    >>> display_board(b)
        0   1   2   3
      +---------------+
    0 | I |   |   |   |
      +---------------+
    1 | l | o | v | e |
      +---------------+
    2 | C | O | M | P |
      +---------------+
    3 | 2 | 0 | 2 |   |
      +---------------+
    >>> b = [[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ', ' ', ' '],\
    [' ', 'c', 'a', 't', 's',' ', ' ', ' ', ' ', ' ',' ', ' ', ' ']]
    >>> display_board(b)
        0   1   2   3   4   5   6   7   8   9  10  11  12
      +---------------------------------------------------+
    0 |   |   |   |   |   |   |   |   |   |   |   |   |   |
      +---------------------------------------------------+
    1 |   | c | a | t | s |   |   |   |   |   |   |   |   |
      +---------------------------------------------------+
    >>> b = [[' ']]
    >>> display_board(b)
        0
      +---+
    0 |   |
      +---+
     
    """
    
    # print a space
    print(end=" ")
    
    # Iterate number of column times
    for i in range(len(board[0])):
        
        # if the number of column is one-digit, print one space more 
        # than if it is two-digit to keep each column aligned with
        # with its correponding number.
        if i < 10:
            print("   " + str(i), end="")
        else:
            print("  " + str(i), end="")
                
    # Go to a new line
    print()
    
    # Assign a variable to the number of dashes that should be displayed to form the line +--...-+ 
    num_of_dashes = (len(board[0])*4) - 1
    
    # Create a variable storing the line +--...-+ that seperates the rows
    line = "  +" + "-"*num_of_dashes + "+"
    
    # iterate number of row times to form the rows
    for row in range(len(board)):
        
        # display the line +--...-+ and go to a new line
        print(line)
        
        # if the number of row is one-digit, print one space more 
        # than if it is two-digit to keep the columns aligned.
        if row < 10:
            print(row, end=" ")
        else:
            print(row, end="")
            
        # iterate number of column times
        for column in range(len(board[0])):
            
            # display a vertical line to seperate the columns and
            # display the corresponding element in each square
            print("| " + board[row][column], end = " ")
            
        # display a vertical line to end each row
        print("|")
    
    # display the line +--...-+  to end the board 
    print(line)
        
def get_vertical_axis(board, col):
    
    """ (list, int) -> list 

    This function takes the board and the number of column as input
    and returns a list of strings containing all the elements from
    board on the specified column.
    
    >>> b = [['c', 'a', 't', ' '], [' ', 'a', 'r', 't'], [' ', ' ', 'a', ' '], \
    [' ', ' ', 'i', ' '], [' ', ' ', 'n', ' ']]
    >>> get_vertical_axis(b, 2)
    ['t', 'r', 'a', 'i', 'n']
    >>> b = [['I',' ',' ',' '],['l','o','v','e'],['C','O','M','P'],['2','0','2',' ']]
    >>> get_vertical_axis(b, 5)
    Traceback (most recent call last):
    IndexError: list index out of range
    >>> get_vertical_axis(b, 0)
    ['I', 'l', 'C', '2']
    >>> get_vertical_axis(b, -4)
    ['I', 'l', 'C', '2']
    
    """
    
    # Create a new list 
    column = []
    
    # iterate through the rows of the board 
    for row in board:
        # append the element in the specified column to the new list 
        column.append(row[col])
    
    # return the specified column
    return column

def find_word(lis, i):
    
    """ (list, i) -> str

    This function returns the string built by concatenating the
    sequence, including i, of consecutive strings from the list
    that are not the space character.
    
    >>> find_word([' ', 'squi', ' ', '', 'rre', 'l', ' '],3)
    'rrel'
    >>> find_word(['','cats','','and',' ','dogs'],0)
    'catsand'
    >>> find_word(['','cats','','and',' ','dogs'],1)
    'catsand'
    >>> find_word(['','cats','','and',' ','dogs'],2)
    'catsand'
    >>> find_word(['','cats','','and',' ','dogs'],3)
    'catsand'
    >>> find_word(['','cats','','and',' ','dogs'],4)
    ''
    >>> find_word(['','cats','','and',' ','dogs'],5)
    'dogs'
    >>> find_word([],0)
    Traceback (most recent call last):
    IndexError: list index out of range
    
    """
    
    # if the the element at index i is a space, return an empty string
    if lis[i]==" ":
        return ""
    
    # Create an empty string 
    returned_word = ""
    
    # iterate backwards from index i until a space is found
    # if a space is found, set j to the letter just after the space
    # if no space is found, set j to 0
    for j in range(i,-1,-1):
        if lis[j] == " ":
            j += 1
            break
    
    # iterate from index j forward
    for k in range(j,len(lis)):
        
        # if a space is encountered, stop iterating 
        if lis[k] == " ":
            break
        
        # if the element is not a space, add it to the returned word
        returned_word += lis[k]
        
    # return the word when all elements are added
    return returned_word

def available_space(lis, i):
    
    """ (list, int) -> int

    This function returns the number of empty squares
    on the input list starting from position i.
    
    >>> r = ['i',' ','l','o','v','e',' ','u']
    >>> available_space(r, 1)
    2
    >>> available_space(r, 3)
    1
    >>> r = ['a', ' ', ' ', 'b', ' ', ' ', 'c', ' ', ' ']
    >>> available_space(r, 2)
    5
    >>> r = [' ']
    >>> available_space(r, 1)
    0
    >>> available_space(r, 0)
    1
    
    """
    
    # Create a variable count representing the number of spaces encountered and set it to 0
    count = 0
    
    # iterate through the list starting from the specified index
    for j in range(i,len(lis)):
        
        # Add 1 to the count if a space is encountered
        if lis[j]==" ":
            count +=1
     
    # return the count 
    return count

def fit_on_board(lis, letters, i):
    
    """ (list, str, int) -> bool
    
    This function returns True if the square in position i is empty and if there
    is enough space on the list to fit all the characters of the word letters
    starting from position i, false otherwise.
    
    >>> r = ['i',' ','l','o','v','e',' ','u']
    >>> fit_on_board(r,'aa',1)
    True
    >>> fit_on_board(r,'a',-2)
    True
    >>> fit_on_board(r,'a',8)
    Traceback (most recent call last):
    IndexError: list index out of range
    >>> r = ['i',' ','l','o','v','e',' ','u',' ']
    >>> fit_on_board(r,'aa',2)
    False
    >>> r = [' ']
    >>> fit_on_board(r,'a',0)
    True
    
    """
    
    # if the square in position i is not empty, return False
    if lis[i] != " ":
        return False
    
    # return True if the number of available spaces starting from i is
    # greater than or equal to the length of letters, false otherwise
    return available_space(lis,i) >= len(letters)
    
    
        
            
        
    
    
        
            
    