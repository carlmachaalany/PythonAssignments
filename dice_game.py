# Name: Carl Machaalani
# ID: 260895058
# A program that stimulates a the Pass Line Bet game

import random

def dice_roll():
    
    """ (None) --> int

    This function returns the sum of two
    randomly rolled six-sided dice.

    >>> random.seed(12)
    >>> dice_roll()
    7
    >>> dice_roll()
    11
    >>> random.seed(2)
    >>> dice_roll()
    2
    >>> dice_roll()
    4
    """
    
    # roll the two dice 
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    
    # return their sum
    summation = roll_1 + roll_2
    return summation

def second_stage(point):
    
    """ (int) --> int

    This function takes an integer (point) as
    input. It returns 7 or point and displays
    a sequence of integers of which the last
    integer is either 7 or point.
    
    >>> random.seed(2)
    >>> r = second_stage(5)
    2 4 8 9 8 7
    >>> r
    7
    >>> random.seed(12)
    >>> r = second_stage(9)
    7
    >>> r
    7
    >>> random.seed(123)
    >>> r = second_stage(8)
    4 5 4 5 10 6 3 5 8
    >>> r
    8
    """
    
    # Assign a variable containing the dice roll
    roll = dice_roll()
    
    # iterate as long as the roll is neither 7 nor point
    while roll not in [7,point]:
        # display roll
        print(roll, end= " ")
        
        # roll again and assign the result to roll
        roll = dice_roll()
    
    # display the last roll (7 or point) on the line
    print(roll)
    
    # return the last roll (7 or point)
    return roll

def can_play(money_wallet, money_bet):
    
    """ (float,float) --> bool

    This function takes the money that the
    user has, money_wallet, and the money
    that the user wants to bet, money_bet,
    as inputs. The function then returns
    True if money_bet is less than money_wallet
    and greater than 0 and returns False otherwise.

    >>> can_play(6.75, 4.5)
    True
    >>> can_play(0.0, 3.0)
    False
    >>> can_play(6.0, 10.0)
    False
    >>> can_play(-5.0, 4.0)
    False
    >>> can_play(5.0, -4.0)
    False
    >>> can_play(0.0,0.0)
    False
    """
    
    # If the bet is between 0 (exclusive) and
    # what the player has (inclusive), return True
    if 0.0 < money_bet <= money_wallet:
        return True
    
    # Otherwise, return False
    return False
    
def pass_line_bet(money_wallet, money_bet):
    
    """ (float,float) --> float

    This function takes the money that the
    user has, money_wallet, and the money
    that the user wants to bet, money_bet,
    as inputs. The function then displays
    the results and returns the amount of
    money the player has left after one
    round of Craps. 
    
    >>> random.seed(12)
    >>> m = pass_line_bet(7.5, 2.5)
    A 7 has been rolled. You win!
    >>> m
    10.0
    >>> random.seed(2)
    >>> m = pass_line_bet(7.5, 2.5)
    A 2 has been rolled. You lose!
    >>> m
    5.0
    >>> random.seed(123)
    >>> m = pass_line_bet(4.0, 4.0)
    A 4 has been rolled. Roll again!
    5 4
    You win!
    >>> m
    8.0
    >>> random.seed(46)
    >>> m = pass_line_bet(10.75, 4.25)
    A 5 has been rolled. Roll again!
    6 7
    You lose!
    >>> m
    6.5
    """
    
    # Assign a variable containing the dice roll
    roll = dice_roll()
    
    # If the roll is 7 or 11, the player wins
    if roll in [7,11]:
        # We display the roll
        print("A",roll,"has been rolled. You win!")
        # We give the player the amount of money he bet
        money_wallet += money_bet
    
    # If the roll is 2, 3, or 12, the player loses
    elif roll in [2,3,12]:
        # We display the roll
        print("A",roll,"has been rolled. You lose!")
        # We take the amount of money the player bet
        money_wallet -= money_bet
    
    # If any other number is rolled, we move to the second stage
    else:
        # We display the roll
        print("A",roll,"has been rolled. Roll again!")
        # Assign a variable containing the result of the second stage
        # The line of results are displayed since we called the function second_stage
        second_round_result = second_stage(roll)
        
        # If the result of the second stage is the point
        if second_round_result == roll:
            print("You win!")
            # We give the player the amount of money he bet
            money_wallet += money_bet
        
        # If the result of the second stage is 7
        else:
            print("You lose!")
            # We take the amount of money the player bet
            money_wallet -= money_bet
     
    # Return the amount of money that the player has left after the game
    return money_wallet

def play():
    
    """ (None) --> None

    This function retrieves the money
    that the player has and the money that
    the player wants to bet. The function
    then plays the pass line bet game, displays
    the results and the amount of money the
    player still has after the game.

    >>> play()
    Please enter your money here: 5.5
    How much would you like to bet? 7.0
    Insufficient funds. You cannot play.
    >>> random.seed(12)
    >>> play()
    Please enter your money here: 7.5
    How much would you like to bet? 2.5
    A 7 has been rolled. You win!
    You now have $10.0
    >>> random.seed(2)
    >>> play()
    Please enter your money here: 7.5
    How much would you like to bet? 2.5
    A 2 has been rolled. You lose!
    You now have $5.0
    >>> random.seed(123)
    >>> play()
    Please enter your money here: 4.0
    How much would you like to bet? 4.0
    A 4 has been rolled. Roll again!
    5 4
    You win!
    You now have $8.0
    >>> random.seed(46)
    >>> play()
    Please enter your money here: 10.75
    How much would you like to bet? 4.25
    A 5 has been rolled. Roll again!
    6 7
    You lose!
    You now have $6.5
    """
    
    # retrieve the money that the player has
    money_wallet = float(input("Please enter your money here: "))
    
    # retrieve the money that the player wants to bet 
    money_bet = float(input("How much would you like to bet? "))
    
    # if the player has enough money to play
    if can_play(money_wallet, money_bet):
        #Assign a variable containing the money that the player has left after the game.
        #By calling the function pass_line_bet, the results are displayed
        money_wallet_left = pass_line_bet(money_wallet, money_bet)
        # Display the money that the player has left rounded to decimal places
        print("You now have $"+str(round(money_wallet_left,2)))
        
    # if the player does not have enough money to play    
    else:
        print("Insufficient funds. You cannot play.")
        
#play()
       

            

    

        
        
        


        
        
        

    
