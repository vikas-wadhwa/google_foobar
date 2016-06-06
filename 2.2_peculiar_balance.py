##########################################################################################################################
##  Google foobar - 2.2 - peculiar_balance.py
##
##  Created by Vikas Wadhwa  http://www.wadhwa-media.com
##########################################################################################################################

##########################################################################################################################
## INSTRUCTIONS
#
# Peculiar balance
# ================
# 
# Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an obstacle. The door will only open if a challenge is solved correctly. The future of the zombified rabbit population is at stake, so Beta reads the challenge: There is a scale with an object on the left-hand side, whose mass is given in some number of units. Predictably, the task is to balance the two sides. But there is a catch: You only have this peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.
# 
# To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where the weights should be placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.
# 
# The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight, and so on. Each string is one of: 
# 
# "L" : put weight on left-hand side 
# "R" : put weight on right-hand side 
# "-" : do not use weight 
# 
# To ensure that the output is the smallest possible, the last element of the list must not be "-".
# 
# x will always be a positive integer, no larger than 1000000000.
# 
# Languages
# =========
# 
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
# 
# Test cases
# ==========
# 
# Inputs:
#     (int) x = 2
# Output:
#     (string list) ["L", "R"]
# 
# Inputs:
#     (int) x = 8
# Output:
#     (string list) ["L", "-", "R"]

##########################################################################################################################



import math
        
    
####################################################################################################################
## Define function to convert incoming weight value to reverse-ordered base-3 (ternary) number string
####################################################################################################################            
def convert_to_backwards_ternary(decimal):
    
    result = ''
    x = decimal
    
    while x > 0 :
        result += str(int(x % 3))
        x = math.floor(x / 3)

    return result
        
        
        
def answer(x):

    result = []
    value = ''
    additional = False    
    backwards_ternary_weight = convert_to_backwards_ternary(x)


    ###############################################################################################################################
    ## As we go from the lower to higher orders in the digits of a ternary number (normally right-to-left but here left-to-right):
    ##
    ##  -  A digit of 0 means there is no weight of this order needing to be added to the righthand scale.
    ##  -  A digit of 1 means that a weight of this order needs to be added to the righthand scale.
    ##  -  Because we only have 1 of each weight, a digit of 2 means that an order of magnitude HIGER than this digit needs 
    ##     to be added to the righthand scale, but a there must be an amount equal to the current digit order added to the
    ##     lefthand scale to compensate
    ###############################################################################################################################
    for n in backwards_ternary_weight:
        
        if n == '0':
            if additional:
                value = 'R'
                additional = False
            else:
                value = '-'
        
        if n == '1':
            if additional:
                value = 'L'
                additional = True
            else:
                value = 'R'
            
        if n == '2':
            if additional:
                value = '-'
                additional = True
            else:
                value = 'L'
                additional = True
    
        result.append(value)
    
    
    ####################################################################################################################
    ## If we have reached the end of the original string and still have a leftover additional component, add it here
    ####################################################################################################################
    if additional:
        result.append('R')



    return result
    

    
