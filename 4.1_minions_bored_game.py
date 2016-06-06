##########################################################################################################################
##  Google foobar - 4.1 - minions_bored_game.py
##
##  Created by Vikas Wadhwa  http://www.wadhwa-media.com
##########################################################################################################################

##########################################################################################################################
## INSTRUCTIONS
#
# Minion's bored game
# ===================
# 
# There you have it. Yet another pointless "bored" game created by the bored minions of Professor Boolean.
# 
# The game is a single player game, played on a board with n squares in a horizontal row. The minion places a token on the left-most square and rolls a special three-sided die. 
# 
# If the die rolls a "Left", the minion moves the token to a square one space to the left of where it is currently. If there is no square to the left, the game is invalid, and you start again.
# 
# If the die rolls a "Stay", the token stays where it is. 
# 
# If the die rolls a "Right", the minion moves the token to a square, one space to the right of where it is currently. If there is no square to the right, the game is invalid and you start again.
# 
# The aim is to roll the dice exactly t times, and be at the rightmost square on the last roll. If you land on the rightmost square before t rolls are done then the only valid dice roll is to roll a "Stay". If you roll anything else, the game is invalid (i.e., you cannot move left or right from the rightmost square).
# 
# To make it more interesting, the minions have leaderboards (one for each n,t pair) where each minion submits the game he just played: the sequence of dice rolls. If some minion has already submitted the exact same sequence, they cannot submit a new entry, so the entries in the leader-board correspond to unique games playable. 
# 
# Since the minions refresh the leaderboards frequently on their mobile devices, as an infiltrating hacker, you are interested in knowing the maximum possible size a leaderboard can have.
# 
# Write a function answer(t, n), which given the number of dice rolls t, and the number of squares in the board n, returns the possible number of unique games modulo 123454321. i.e. if the total number is S, then return the remainder upon dividing S by 123454321, the remainder should be an integer between 0 and 123454320 (inclusive).
# 
# n and t will be positive integers, no more than 1000. n will be at least 2.
# 
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
#     (int) t = 1
#     (int) n = 2
# Output:
#     (int) 1
# 
# Inputs:
#     (int) t = 3
#     (int) n = 2
# Output:
#     (int) 3
##########################################################################################################################


def answer(t, n):

    # there are no solutions if there are not enough dice rolls to get you to the rightmost square
    if t < n-1 :
        return 0
        
    # there is only one solution, all right rolls, if you have just enough rolls to get to the right.   
    elif t == n-1 :
        return 1
        
    #since we start on square 1, we need to transverse n-1 squares over t moves    
    else :
        
        ##########################################################################################################################
        ##  Given that calculating even just the possible combinations for JUST rolling RIGHTs and STAYs is
        ##    t! / (t-n-1)!(n-1)!  
        ##    where (t-n-1) = Number of STAYs, given the needed (n-1) RIGHTs.
        ##  
        ##  and that every combination of possible LEFT rolls is an algorithm that will need to iterate over the range of possible
        ##  LEFT rolls that are available...we're going to take a simpler approach and loop through the turns presented and 
        ##  count up how many get us to stay on the actual rightmost square.
        ##
        ##  We generate a dictionary of positions on the board (starting with 1) and the count of paths that lead to that position
        ##  example: end = {1:1, 2:1} after 1 turn
        ##########################################################################################################################
        end = {1:1}
        
        for turn in range(t):

            # Start the next turn independently from the results of the last turn
            start = end
            
            # The incoming values are a sum of the paths to get to square 'position' in turn 'turn'. This means each turn needs to 
            # reset the counter and sum up the path counts generated from the new turn.
            end = {}
            
            for position, count in start.iteritems():
                
                # the first box can only roll STAY or RIGHT        
                if position==1:
                    rolls = [0,1]   
                    
                # the last box can only roll STAY
                elif position == n:
                    rolls = [0]
                
                else:
                    rolls = [-1,0,1]
                    
                # every count represents the number of ways to get to that square. Every movement FROM that start square then
                # represents a possible path to the END square. Total up the counts from everything on this turn that winds up
                # on a given square.
                for r in rolls:
                    end.setdefault(position + r, 0)
                    end[position + r] += count
            
        return end[n] % 123454321