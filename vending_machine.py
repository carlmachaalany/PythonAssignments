#Name: Carl Machaalani
# ID: 260895058
#A program that stimulates a virtual vending machine

#Assigning variables that store the amount of coins present in the machine for each type of coin
TOONIES = 10/2
LOONIES = 5/1
QUARTERS = 5/0.25
DIMES = 3/0.1
NICKELS = 2/0.05

def display_welcome_menu():
    
    """ (None) -> None

    This function welcomes the user
    and provides a list with all the
    options available to the customer.
    
    >>> display_welcome_menu()
    Welcome to COMP 202 Virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    
    """
    
    #Welcoming the user to the Virtual Vending Machine with a list of options
    print("Welcome to COMP 202 Virtual Vending Machine!")
    print("Here are your options:")
    print("1. Candy bar $2.95")
    print("2. Cookies $3.90")
    print("3. Soda $4.00")
    print("4. Chips $3.90")
    print("5. No snacks for me today!")
    
def get_snack_price(option):
    
    """ (num) -> int

    This function takes an option as a prameter and
    returns the value of the option in cents. If the
    option is not from 1 till 4 inclusive, the function
    returns the value 0.
    
    >>> get_snack_price(2)
    390
    >>> get_snack_price(3)
    400
    >>> get_snack_price(5)
    0
    >>> get_snack_price(-4)
    0
    >>> get_snack_price(1.2)
    0
    >>> get_snack_price(0)
    0
    """
    
    #Returning the value in cents of each option
    if (option == 1): 
        return 295
    elif (option == 2 or option == 4):
        return 390
    elif (option == 3):
        return 400
    #If no option available has been picked, the function returns the value 0 
    else: 
        return 0
    
def get_num_of_coins(change, value_coin , coins_in_machine):
    
    """ (num,num,num) -> num

    This function takes the change, the value of a coin (value_coin),
    and the numbers of coins in the machine (coins_in_machine) and
    returns the maximum number of coins of the given value that can
    be used to fulfill the amount of change.
    
    >>> get_num_of_coins(2500, 200, 4)
    4
    >>> get_num_of_coins(760, 100, 8)
    7
    >>> get_num_of_coins(123, 25, 7)
    4
    >>> get_num_of_coins(140, 10, 14)
    14
    >>> get_num_of_coins(90, 100, 5)
    0
    >>> get_num_of_coins(122.7, 10.1, 16.2)
    12.0
    """
    
    #Calculating the maximum number of coins for a given value of coin to fulfill the change 
    num_coins_needed = change//value_coin
    
    #If the maximum number of coins is greater or equal to the coins provided by the machine,
    if (num_coins_needed >= coins_in_machine):
        #return the coins provided by the machine
        return coins_in_machine
    
    #If the maximum number of coins is less than the coins provided by the machine,
    else:
        #return the maximum number of coins
        return num_coins_needed                

def compute_and_display_change(change):
    
    """ (num) -> bool

    This function takes a non-negative change as a parameter to compute
    and display the number of coins that should be given for each type
    of coin to the user with the least amount of coins possible and returns
    True. The change must not be a multiple of 5 nor greater than the money
    that the machine has which is 2500 cents or else the function will display
    a complaint and return False.
    
    >>> compute_and_display_change(780)
    Here is your change:
     toonies x 3
     loonies x 1
     quarters x 3
     dimes x 0
     nickles x 1
    True
    >>> compute_and_display_change(147)
    No pennies are accepted
    False
    >>> compute_and_display_change(3400)
    The machine does not have enough coins to provide you with the change
    False
    >>> compute_and_display_change(2783)
    No pennies are accepted
    False
    """
    
    #Calculate max number of toonies that can be returned to approach our goal
    toonies_change = get_num_of_coins(change, 200, TOONIES)
    
    #Calculate the amount left in cents after adding the toonies
    amount_left = change - (toonies_change*200)
    #Calculate max number of loonies that can be returned to approach our goal
    loonies_change = get_num_of_coins(amount_left, 100, LOONIES)
    
    #Calculate the amount left in cents after adding the toonies and loonies
    amount_left -= loonies_change*100
    #Calculate max number of quarters that can be returned to approach our goal
    quarters_change = get_num_of_coins(amount_left, 25, QUARTERS) 
    
    #Calculate the amount left in cents after adding the toonies,loonies, and quarters
    amount_left -= quarters_change*25
    #Calculate max number of dimes that can be returned to approach our goal
    dimes_change = get_num_of_coins(amount_left, 10, DIMES)
    
    #Calculate the amount left in cents after adding the toonies,loonies,quarters, and dimes
    amount_left -= dimes_change*10
    #Calculate max number of nickels that can be returned to approach our goal
    nickels_change = get_num_of_coins(amount_left, 5, NICKELS)
    
    #if the change is not a multiple of 5, then the money paid by the user is also not a multiple of 5
    if ((change % 5) != 0):  
        return False
    #if the amount left is not 0, then the change was greater than the money in the machine
    elif (change > 2500):  
        return False
    #if the change is multiple of 5 and money paid less than or equal to the money in the machine, the changes are displayed
    else: 
        print("Here is your change:")
        print(" toonies x",int(toonies_change))
        print(" loonies x",int(loonies_change))
        print(" quarters x",int(quarters_change))
        print(" dimes x",int(dimes_change))
        print(" nickles x",int(nickels_change))
        print("Thank you for stopping by!")
        return True

    
def operate_machine():
    
    """ (None) -> None

    This function displays a welcome for the user and provides a list of
    options of which the user should choose from. The function then displays
    the value in cents of the option chosen and takes as input the amount of
    money in dollars that the user is paying. The function then displays this
    amount in cents and the change for each type of coin. If one of the steps
    does not work out as it should, the function will complain and end the
    execution of the function.
    
    >>> operate_machine()
    Welcome to COMP 202 Virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 2
    The item of your choice costs 390 cents
    Enter your money: $4.5
    You inserted 450 cents
    You should receive back 60 cents
    Here is your change:
     toonies x 0
     loonies x 0
     quarters x 2
     dimes x 1
     nickles x 0
     
    >>> operate_machine()
    Welcome to COMP 202 Virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 5
    Nothing for you today. Thank you for stopping by!
    
    >>> operate_machine()
    Welcome to COMP 202 Virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 3
    The item of your choice costs 400 cents
    Enter your money: $2.6555555
    You inserted 266 cents
    The cash is not enough. Come by another time!
    
    >>> operate_machine()
    Welcome to COMP 202 Virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 8
    Not a valid option! Goodbye!
    
    >>> operate_machine()
    Welcome to COMP 202 Virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 4
    The item of your choice costs 390 cents
    Enter your money: $4.32
    You inserted 432 cents
    No pennies are accepted
    
    >>> operate_machine()
    Welcome to COMP 202 Virtual Vending Machine!
    Here are your options:
    1. Candy bar $2.95
    2. Cookies $3.90
    3. Soda $4.00
    4. Chips $3.90
    5. No snacks for me today!
    Please select your choice: 1
    The item of your choice costs 295 cents
    Enter your money: $3400
    You inserted 340000 cents
    The machine does not have enough coins to provide you with the change :(
     """
    
    display_welcome_menu()
    
    #Take option as input from user, turn it into an integer, and store it as a variable
    option = int(input("\nPlease select your choice: ")) 
    
    #If one of the available items was chosen
    if (1 <= option <= 4):
        
        #the price of item is displayed
        print("\nThe item of your choice costs",get_snack_price(option),"cents")
        
        #Take the user's money as input, turn it into a float, and store it as a variable
        money_inserted = float(input("Enter your money: $"))
        
        #Rounding the user's money to two decimal places
        money_inserted_rounded = round(money_inserted, 2)
        
        #converting the user's money from dollars to cents
        money_inserted_in_cents = int(money_inserted_rounded*100)
        
        print("\nYou inserted",money_inserted_in_cents,"cents")
        
        #calculating the change that should be given back to the user
        change = (money_inserted_in_cents) - (get_snack_price(option)) 
        
        #If the change is greater than the amount in the machine    
        if (change > 2500):
            print("The machine does not have enough coins to provide you with the change :( ")
            
        #If the money inserted by the user is not enough to cover the item's price
        elif (change < 0): 
            print("The cash is not enough. Come by another time!")
            
        #if the money paid by the user is not a multiple of 5
        elif (money_inserted_in_cents%5 != 0):
            print("No pennies are accepted :(")
            
        #If all is good, change is computed and displayed
        else:           
            print("You should receive back",change,"cents\n")
            compute_and_display_change(change) 
    
    #If option 5 was displayed, an ending statement is displayed and the function execution ends
    elif (option == 5): 
        print("Nothing for you today. Thank you for stopping by!")
        
    #If none of the options provided was displayed, an ending statement is displayed and the function execution ends
    else:              
        print("Not a valid option! Goodbye!")
        
#operate_machine()
        
