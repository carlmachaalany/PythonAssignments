# Name: Carl Machaalani
# ID: 260895058


# Question 1
def brick_tower(nb_large_bricks, nb_small_bricks, height):
    
    """ (int, int, int) -> bool
    
    This function takes the number of large bricks, the number
    of small bricks, and the height of the tower we need to
    build as input. The function then returns True if a brick
    tower of the specified height can be built from the available
    bricks, False otherwise.
    
    >>> brick_tower(1, 2, 17)
    False
    >>> brick_tower(2, 4, 22)
    True
    >>> brick_tower(1, 9, 18)
    True
    >>> brick_tower(3, 2, 17)
    False
    >>> brick_tower(3, 2, 0)
    True
    """
    
    if height == 0:
        return True
    
    # if the height is even 
    elif height%2 == 0:
        
        # First, we look at the large bricks. We should only add portions of 2
        # so that the remaining height stays even in order for it to be possible
        # to complete the height with the small bricks.
        
        # if we have enough large bricks to add the maximum possible number of 2 portions that we can add
        if (height//14)*2 <= nb_large_bricks:
            height -= (height//14) * 14
        
        # if it's not enough, we add the maximum even number of large bricks
        elif nb_large_bricks%2 == 0:
            height -= nb_large_bricks * 7
            
        else:
            height -= (nb_large_bricks - 1) * 7
        
        # We then go to the small bricks. If there are enough small
        # bricks to complete the remaining height, we return True
        if height//2 <= nb_small_bricks:
            return True
    
    # If the height is odd
    else:
        
        # First, we look at the large bricks. We should only add an odd number
        # so that the remaining height becomes even in order for it to be possible
        # to complete the height with the small bricks.
        
        # if we have enough large bricks to add the maximum possible 
        # number that we can add and this number is odd
        if (height//7 <= nb_large_bricks) and (height//7)%2 != 0:
            height -= (height//7) * 7
       
        # Otherwise, if we don't have enough large bricks to add the max
        # possible number that we can add and the number of large bricks
        # available is odd, we add all the large bricks available
        elif (height//7 > nb_large_bricks) and (nb_large_bricks%2 != 0):
            height -= nb_large_bricks * 7
        
        # if it's the same case as the previous one but
        # the number of large bricks available is even
        else:
            height -= (nb_large_bricks-1) * 7
        
        # We then go to the small bricks. If one of the above conditional
        # statements is executed and there are enough small bricks to
        # complete the remaining height, we return True
        if height%2 == 0 and height//2 <= nb_small_bricks:
                return True
    
    # We return False if can't build a brick tower
    return False


# Question 2
def get_triangle(n, s):
    
    """ (int, str) -> str
    
    This function takes the triangle's height n and a symbol
    s as input and returns a triangle with n as its height
    and s as the symbol used to draw it. if n is negative or
    s does not contain at least one character, a ValueError
    is raised.
    
    >>> d = get_triangle(3, '$')
    >>> print(d)
    $ 
    $ $ 
    $ $ $ 
    $ $ 
    $ 

    >>> e = get_triangle(1, '*')
    >>> print(e)
    * 

    >>> f = get_triangle(0, 'm')
    >>> print(f)

    >>> g = get_triangle(-2, 'i')
    Traceback (most recent call last):
    ValueError: The first input should be negative
    >>> h = get_triangle(3, '')
    Traceback (most recent call last):
    ValueError: The string must contain at least one character
    """
    
    if n<0:
        raise ValueError('The first input should be negative')
    
    # I seperated them because I want  each case to display a different message
    if len(s) == 0:
        raise ValueError('The string must contain at least one character')
    
    triangle = ''
    for i in range(1, n):
        triangle += i * (s + ' ') + '\n'
    
    for j in range(n, 0, -1):
        triangle += j * (s + ' ') + '\n'
        
    return triangle


# Question 3
def sort_numbers(lis):
    
    """ (list) -> NoneType
    
    This function modifies the input list of integers so that all the
    even numbers are at the beginning and all the odd numbers are
    at the end.
    
    >>> a = [5, -6, 2, 3, -1, 0]
    >>> sort_numbers(a)
    >>> a
    [-6, 2, 0, 5, 3, -1]
    >>> a = []
    >>> sort_numbers(a)
    >>> a
    []
    >>> a = [1, 3, 5, 7, 2, 4, 6, 8]
    >>> sort_numbers(a)
    >>> a
    [2, 4, 6, 8, 1, 3, 5, 7]
    >>> a = [1, 1, 2, 3, 2]
    >>> sort_numbers(a)
    >>> a
    [2, 2, 1, 1, 3]
    """
    
    i = 0
    iterations = 0
    
    while iterations < len(lis):
        
        # if the integer is odd, bring it to the end of the list
        if lis[i]%2 != 0:
            
            integer = lis.pop(i)
            lis.append(integer)
            
            # we keep the index as is so that we don't skip the following integer
            i -= 1
            
        i += 1
        iterations += 1
 
 
# Question 4
def select_vector(x, y):
    
    """ (list, list) -> list
    
    This function takes a 2D list of integers x and a 1D list of
    integers y. The function then returns a 1D list of integers
    containing the elements of the sublists of x which appear in
    the position specified by y. The function raises a ValueError
    if either y doesn't contain the same number of elements as x
    or the indices of y are out of bounds.
    
    >>> select_vector([[2, 1, 9], [4, 2], [9, 6, -5, 1]], [-2, 0, 2])
    [1, 4, -5]
    >>> select_vector([[2, 1, 9], [4, 2], [9, 6, -5, 1]], [-2, 0])
    Traceback (most recent call last):
    ValueError: The two lists must contain the same number of elements
    >>> select_vector([[2, 1, 9], [4, 2], [9, 6, -5, 1]], [1, 2, 0])
    Traceback (most recent call last):
    ValueError:  At least one of the indices is out of bounds
    >>> select_vector([[2], [4], []], [0, 0, 0])
    Traceback (most recent call last):
    ValueError:  At least one of the indices is out of bounds
    """

    if len(x) != len(y):
        raise ValueError("The two lists must contain the same number of elements")
    
    returned_list = []
    
    for i, index in enumerate(y):
                
        if index not in range(-len(x[i]), len(x[i])):
            raise ValueError(" At least one of the indices is out of bounds")
         
        returned_list.append(x[i][index])
    
    return returned_list


# Question 5
def get_coordinates(w, target):
    
    """ (list, str) -> list
    
    This function takes a 2D list of strings w and a
    string target as input returns a list of tuples
    representing the indices of where the target
    appears in w.
    
    >>> l = [['e', 'q', 'w', 'Q'], ['e', 'r', 'q', 'e'], ['E', 'e', 's', '']]
    >>> t = get_coordinates(l, 'q')
    >>> t
    [(0, 1), (1, 2)]
    >>> t = get_coordinates(l, 'e')
    >>> t
    [(0, 0), (1, 0), (1, 3), (2, 1)]
    >>> l = [[' ', 'bull'], ['Bull', 'bull', 'bulldog'], ['BULL', 'bull']]
    >>> t = get_coordinates(l, 'bull')
    >>> t
    [(0, 1), (1, 1), (2, 1)]
    >>> l = []
    >>> t = get_coordinates(l, '')
    >>> t
    []
    """
    
    returned_list = []
    
    for i in range(len(w)):
        
        for j in range(len(w[i])):
            
            if w[i][j] == target:
                returned_list.append((i, j))
                
    return returned_list


# Question 6
def evaluate_polynomial(polynomial, x):
    
    """ (dict, num) -> num

    This function takes a dictionary representing a polynomial
    and a number x as input and returns the value of the
    polynomial for the given value of x.
    
    >>> evaluate_polynomial({2: -2, 1: 2, 0: 7}, 2)
    3
    >>> evaluate_polynomial({3: -2, 1: 3, 0: 4.2}, 2.5)
    -19.55
    >>> evaluate_polynomial({1: 4, 4: -1, 2: 0, 0: 1}, 2.5)
    -28.0625
    >>> evaluate_polynomial({}, 2)
    0
    """
    
    value = 0
    
    for key in polynomial:
        
        value += (x**key) * polynomial[key]
    
    return value


# This is a helper function for question 7
def get_occurrences(string):
    
    """ (str) -> dict

    This function takes a string as input and returns
    a dictionary where the keys are the characters in
    the string and the values are their corresponding
    number of occurences in the string.
    
    >>> d = get_occurrences('mama')
    >>> d == {'m':2, 'a':2}
    True
    >>> d = get_occurrences('')
    >>> d == {}
    True
    >>> d = get_occurrences('mississipi')
    >>> d == {'m':1, 'i':4, 's':4,'p':1}
    True
    >>> d = get_occurrences("you're")
    >>> d == {'y':1, 'o':1, 'u':1, "'":1, 'r':1, 'e':1}
    True
    
    """
    
    # Create an empty dictionary
    dic = {}
    
    # iterate though the characters of the string
    for char in string:
        
        char = char.lower()
        
        # if the chararacter is in the dictionary, add 1 to its value
        # if the character is not in the dictionary, add it and set its value to 1 
        dic[char] = dic.get(char, 0) + 1
         
    # return the dictionary
    return dic

# Question 7
def anagrams(list_of_str , string):
    
    """ (list, str) -> bool
    
    This function returns True if the list contains only
    anagrams of the specified string, false otherwise.

    >>> anagrams(['Tabs', 'STAB', 'bats'], 'bats')
    True
    >>> anagrams(['back', 'BACK', 'bak'], 'back')
    False
    >>> anagrams(['212333', '321332', '122333'], '122333')
    True
    >>> anagrams([' ', ' ', ' '], ' ')
    True
    >>> anagrams(['', '', ''], '')
    True
    """
    
    occurrences_string = get_occurrences(string)
    
    for element in list_of_str:
        
        if get_occurrences(element) != occurrences_string:
            return False
    
    return True


# This is a helper function for question 8
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

# This is a helper function for question 8
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

# Question 8        
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
    
    import random
    
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

# Question 9 
class Cake:
    
    """
    Instance Attributes: name(str), ingreds(list), price(float)
    """
        
    def __init__(self, cake_name, ingredients):
        
        import random
        
        self.name = cake_name
        
        if len(ingredients) < 3:
            raise ValueError("The cake must have at least 3 ingredients")
        self.ingreds = ingredients
        
        self.price = random.randint(10,14) + random.random()
        
    def __str__(self):
        
        """ (Cake) -> str
        
        This function returns the name and the price of the
        input cake rounded to 2 decimal places.
        
        >>> random.seed(3)
        >>> t = Cake('Bahamas', ['banana', 'cream', 'chocolate'])
        >>> print(t)
        Bahamas $11.59
        >>> t = Cake('Vanilla Cake', ['vanilla', 'eggs', 'butter', 'cream'])
        >>> print(t)
        Vanilla Cake $11.37
        >>> t = Cake('Sponge Cake', ['sponge', 'eggs'])
        Traceback (most recent call last):
        ValueError: The cake must have at least 3 ingredients
        """
        
        rounded_price = round(self.price, 2)
        
        return self.name + ' $' + str(rounded_price)
    
    def is_better(self, other_cake):
        
        """ (Cake, Cake) -> bool
        
        This function returns True if the current cake has a
        better (lower) price:number of ingredients ratio than
        the other input cake, False otherwise.
        
        
        >>> random.seed(3)
        >>> t = Cake('Vanilla Cake', ['vanilla', 'cream', 'sugar'])
        >>> t.price
        11.592640910627166
        >>> other = Cake('Bahamas', ['banana', 'cream', 'sugar', 'chocolate'])
        >>> other.price
        11.36995516654808
        >>> another = Cake('Chocolate', ['cream', 'sugar', 'chocolate'])
        >>> another.price
        14.474053536547126
        >>> t.is_better(other)
        False
        >>> other.is_better(t)
        True
        >>> t.is_better(another)
        True
        >>> another.is_better(other)
        False
        >>> t.is_better(t)
        False
        """
        
        my_cake_ratio = self.price / len(self.ingreds)
        
        other_cake_ratio = other_cake.price / len(other_cake.ingreds)
        
        return my_cake_ratio < other_cake_ratio
    
def create_menu(dict_cakes):
    
    """ (dict) -> list
    
    This function takes a dictionary mapping cake names to their list
    of ingredients and returns a list of Cake objects. The function
    also displays the menu.
    
    >>> random.seed(3)
    >>> d = {'Genoise Cake': ['egg', 'genoise', 'nuts'], 'Chiffon Cake': ['chiffon', 'cream', 'sugar'],\
                 'Yellow Butter Cake': ['butter', 'flour', 'cream']}
    >>> t = create_menu(d)
    Genoise Cake $11.59
    Chiffon Cake $11.37
    Yellow Butter Cake $14.47
    >>> t
    [<__main__.Cake object at 0x104e11c90>, <__main__.Cake object at 0x104e11e90>, <__main__.Cake object at 0x104e11d50>]
    >>> t[0].ingreds
    ['egg', 'genoise', 'nuts']
    >>> t[2].name
    'Yellow Butter Cake'
    >>> t[1].price
    11.36995516654808
    >>> d = {'Sponge Cake': ['egg', 'sugar', 'chocolate'], 'Red Velvet Cake': ['red velvet', 'cream', 'sugar'], \
                 'Pound Cake': ['butter', 'flour', 'pound']}
    >>> t = create_menu(d)
    Sponge Cake $14.07
    Red Velvet Cake $10.91
    Pound Cake $13.26
    >>> t
    [<__main__.Cake object at 0x104e12690>, <__main__.Cake object at 0x104e11e10>, <__main__.Cake object at 0x104e117d0>]
    >>> t[0].name
    'Sponge Cake'
    >>> t[1].ingreds
    ['red velvet', 'cream', 'sugar']
    >>> t[2].price
    13.259354014328007
    >>> d = {'Bahamas': ['banana', 'cream', 'sugar', 'chocolate'], 'Vanilla Cake': ['vanilla', 'cream', 'sugar'], \
                 'Chocolate': ['cream', 'sugar', 'chocolate']}
    >>> t = create_menu(d)
    Bahamas $11.19
    Vanilla Cake $13.54
    Chocolate $14.48
    >>> t
    [<__main__.Cake object at 0x104e11dd0>, <__main__.Cake object at 0x104e116d0>, <__main__.Cake object at 0x104e11c50>]
    >>> t[0].ingreds
    ['banana', 'cream', 'sugar', 'chocolate']
    >>> t[1].price
    13.54097388562904
    >>> t[2].name
    'Chocolate'
    """
    
    returned_list = []
    
    for name in dict_cakes:
        
        cake = Cake(name, dict_cakes[name])
        
        returned_list.append(cake)
        
        print(cake)
        
    return returned_list

def find_best(list_of_cakes):
    
    """ (list) -> Cake
    
    This function takes a list of cakes as input 
    and returns the best cake in the list. If
    there are ties, the function returns the
    first best cake.
    
    >>> random.seed(3)
    >>> t = Cake('Vanilla Cake', ['vanilla', 'cream', 'sugar'])
    >>> t.price
    11.592640910627166
    >>> other = Cake('Bahamas', ['banana', 'cream', 'sugar', 'chocolate'])
    >>> other.price
    11.36995516654808
    >>> another = Cake('Chocolate', ['cream', 'sugar', 'chocolate'])
    >>> another.price
    14.474053536547126
    >>> another_2 = Cake('Sponge Cake', ['egg', 'sugar', 'chocolate'])
    >>> another_2.price
    14.065528859239812
    >>> m = find_best([t, other, another])
    >>> m
    <__main__.Cake object at 0x106a239d0>
    >>> print(m)
    Bahamas $11.37
    >>> m.ingreds
    ['banana', 'cream', 'sugar', 'chocolate']
    >>> s = find_best([t, another, another_2])
    >>> s
    <__main__.Cake object at 0x106a23d90>
    >>> print(s)
    Vanilla Cake $11.59
    >>> s.ingreds
    ['vanilla', 'cream', 'sugar']
    >>> n = find_best([another, another_2])
    >>> n
    <__main__.Cake object at 0x106a23b10>
    >>> print(n)
    Sponge Cake $14.07
    >>> n.ingreds
    ['egg', 'sugar', 'chocolate']
    """
    
    best_cake = list_of_cakes[0]
    
    for cake in list_of_cakes:
        
        if cake.is_better(best_cake):
            
            best_cake = cake
    
    return best_cake
        
        
        
        
        
    

    
    
    
    
    
                
    
    
    
    
        
        
        
