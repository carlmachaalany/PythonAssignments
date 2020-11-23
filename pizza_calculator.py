#Name: Carl Machaalani
# ID: 260895058
# A program that calculates the fair quantity or fair price when buying pizzas

#Importing pi function from math module
from math import pi

def display_welcome_menu():
    
    """ (None) -> None
    
    This function welcomes the user to the
    fair pizza caluclator and provides the
    user with two choices of modes.
    
    >>> display_welcome_menu()
    Welcome to COMP 202 fair pizza calculator!
    Please choose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    
    """
    
    print("Welcome to COMP 202 fair pizza calculator!")
    print("Please choose one of the following modes:")
    print('A. "Quantity mode"')
    print('B. "Price mode"')

def get_fair_quantity(diameter_1, diameter_2):
    
    """ (num, num) -> int

    This function takes the diameter of two pizzas
    diameter_1 and diameter_2 as parameters and returns
    an integer indicating the minimum number of the
    smaller pizza one should order so that he gets
    at least the same amount of the larger pizza.
    
    >>> get_fair_quantity(8,8)
    1
    >>> get_fair_quantity(15,7)
    5
    >>> get_fair_quantity(6,13)
    5
    >>> get_fair_quantity(7.5, 15.2)
    5
    """
    
    #We assign the variables diameter_large_pizza and diameter_small_pizza to the
    #larger and smaller pizzas respectively. If equal, we return the value 1.
    if (diameter_1 > diameter_2):  
        diameter_large_pizza = diameter_1
        diameter_small_pizza = diameter_2
    elif (diameter_1 < diameter_2):
        diameter_large_pizza = diameter_2
        diameter_small_pizza = diameter_1
    else:
        return 1
    
    # Calculating the radius of each pizza
    radius_large_pizza = diameter_large_pizza/2
    radius_small_pizza = diameter_small_pizza/2
    
    # Calculating the area of each pizza
    area_large_pizza = pi * (radius_large_pizza**2)
    area_small_pizza = pi * (radius_small_pizza**2)
    
    #Dividing the area of the larger pizza over the area of the smaller pizza and rounding up to the nearest integer
    fair_num_of_pizza = int((area_large_pizza/area_small_pizza) + 1)
    return fair_num_of_pizza

def get_fair_price(diameter_of_large_pizza, price_of_large_pizza, diameter_of_small_pizza, num_small_pizzas):
    
    """ (num, num, num, int) -> num

    This function takes as parameters: the diameter of the large pizza
    diameter_of_large_pizza, the price of the large pizza price_of_large_pizza,
    the diameter of the small pizza diameter_of_small_pizza, and the number of
    small pizzas that the user is ordering. The function returns the fair price
    that the user should pay for the small pizzas , that is, the price such that
    the amount of pizza per dollar is the same as that of the larger pizza.The
    return value gives the answer with two decimal points.
    
    >>> get_fair_price(11, 12.25, 4, 3)
    4.86
    >>> get_fair_price(15, 16, 7, 2)
    6.97
    >>> get_fair_price(7.5, 9.23, 5.4, 1)
    4.78
    """
    
    #Compute the area of the large pizza
    radius_of_large_pizza = diameter_of_large_pizza/2
    area_of_large_pizza = pi * (radius_of_large_pizza**2)
    
    #Compute the area of the small pizzas
    radius_of_small_pizza = diameter_of_small_pizza/2
    area_of_1_small_pizza = pi * (radius_of_small_pizza**2)
    area_of_small_pizzas = area_of_1_small_pizza * num_small_pizzas
    
    #Compute the amount of pizza per dollar
    amount_of_pizza_per_dollar = area_of_large_pizza / price_of_large_pizza
    
    #Compute the total price of small pizzas and returning it rounded to two decimal places
    total_price_of_small_pizzas = area_of_small_pizzas / amount_of_pizza_per_dollar
    return round(total_price_of_small_pizzas, 2)

def run_pizza_calculator():
    
    """ (None) -> None

    This function welcomes the user and provides him with two choices of
    modes. The function then takes the choice of the user as input. If the
    user enters a mode that is not available, the function will display a
    statement that indicates that the mode entered is not supported and
    ends the execution of the function. If the mode entered is A (quantity mode),
    the function retrieves from the user two inputs indicating the diameters of
    two pizzas and displays back the number of the smaller pizzas that the user
    should take in order to cover the amount of pizza of the large pizza. If
    the mode entered is B (price mode), the function retrieves from the user
    four inputs indicating the diameter of a large pizza, the price of a large
    pizza, the diameter of a small pizza, and the number of small pizzas the user
    wants to get. The function will then display the fair price to pay for the
    small pizzas.
    
    >>> run_pizza_calculator()
    Welcome to COMP 202 fair pizza calculator!
    Please choose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: A

    You selected "Quantity mode"

    Enter the diameter of the large pizza: 8
    Enter the diameter of the small pizza: 3 

     To be fully satisfied, you should order 8 small pizzas.
     
    >>> run_pizza_calculator()
    Welcome to COMP 202 fair pizza calculator!
    Please choose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: B

    You selected "Price mode"

    Enter the diameter of the large pizza: 8
    Enter the price of the large pizza: 7
    Enter the diameter of the small pizza: 5
    Enter the number of small pizzas you'd like to buy: 3

    The fair price to pay for 3 small pizzas is $ 8.2
    
    >>> run_pizza_calculator()
    Welcome to COMP 202 fair pizza calculator!
    Please choose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: 7
    This mode is not supported
    
    >>> run_pizza_calculator()
    Welcome to COMP 202 fair pizza calculator!
    Please choose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: b
    This mode is not supported
    """
    
    display_welcome_menu()
    
    #provide the user for choice of mode
    choice = input("Enter your choice: ") 
    
    if (choice == "A"):
        print('\nYou selected "Quantity mode"\n')
        #take first diameter as input
        diameter_1 = float(input("Enter the diameter of the large pizza: "))
        #take second diamter as input
        diameter_2 = float(input("Enter the diameter of the small pizza: ")) 
        #display fair quantity
        print("\n To be fully satisfied, you should order",get_fair_quantity(diameter_1, diameter_2),"small pizzas.") 
    
    elif (choice == "B"):
        print('\nYou selected "Price mode"\n')
        #take diameter of large pizza as input
        diameter_of_large_pizza = float(input("Enter the diameter of the large pizza: "))
        #take price of large pizza as input
        price_of_large_pizza = float(input("Enter the price of the large pizza: "))
        #take diameter of small pizza as input
        diameter_of_small_pizza = float(input("Enter the diameter of the small pizza: "))
        #take number of small pizzas the user wants as input
        num_small_pizzas = int(input("Enter the number of small pizzas you'd like to buy: "))
        #display fair price
        print("\nThe fair price to pay for",num_small_pizzas,"small pizzas is $",
              get_fair_price(diameter_of_large_pizza, price_of_large_pizza, diameter_of_small_pizza, num_small_pizzas))
        
    #if option entered was not available, display end statement and end execution
    else:
        print("This mode is not supported") 
run_pizza_calculator()

