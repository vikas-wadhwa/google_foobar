##########################################################################################################################
##  Google foobar - 4.2 - breeding_like_rabbits.py
##
##  Created by Vikas Wadhwa  http://www.wadhwa-media.com
##########################################################################################################################

##########################################################################################################################
## INSTRUCTIONS
#
# Breeding like rabbits
# =====================
# 
# As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci sequence like all good rabbits do, the zombit population changes according to this bizarre formula, where R(n) is the number of zombits at time n:
# 
# R(0) = 1
# R(1) = 1
# R(2) = 2
# R(2n) = R(n) + R(n + 1) + n (for n > 1)
# R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)
# 
# (At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)
# 
# Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by playing a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion objected that this was too easy, and proposed a slightly different game: when is the last time that the zombit population will be equal to a certain amount? And thus, much fun was had, and much merry was made.
# 
# (Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)
# 
# Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S will be a positive integer no greater than 10^25.
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
#     (string) str_S = "7"
# Output:
#     (string) "4"
# 
# Inputs:
#     (string) str_S = "100"
# Output:
#     (string) "None"
##########################################################################################################################



##  Create a memoization dictionary to store population values as we calculate them.
##  populations = {time n:population at time n}
populations = {0:1, 1:1, 2:2}


def answer(str_S):
    population = int(str_S)
    ##########################################################################################################################
    ##  A look at the recursion relation shows that even-valued times increase faster than odd-valued times because of the
    ##  addition of n in the even relations vs the addition of 1 in the odd relations. This means that it takes longer for
    ##  an odd relation to get to a given population (if at all, of course) and, therefore, we should search values of odd time
    ##  that lead to a given population. If no odd time is found, then search even times. If none found there, then return None.
    ##########################################################################################################################
    # we need to quickly find an upper bound.
    end = find_end(population)

    # search through odd populations first, i==1. Then even is i==0.
    for i in [1, 0]:
    
        n = i
        start = i

        #  For the seed cases, we examine the upper bound first, then proceed to the search.
        x = end
        
        while True:

            # if the search just leads us to the same value again, the population isn't found, so exit this loop.
            if x == n :
                break
            else:
                n = x

            ##########################################################################################################################
            ## calculate the population from the new search value:
            ## - if the input time generates the population we're looking for, return this input time as the answer. 
            ## - else if the search value gives a result lower than the input population, search again using this as a lower bound
            ## - else if the search value gives a result higher than the input population, search again using this as an upper bound
            ##########################################################################################################################            
            result = R(n)       
             
            if result == population:
                return n

            elif result < population:
                start = n + 1

            elif result > population:
                end = n - 1
                              
            ##########################################################################################################################
            ## Search in the middle of the upper and lower bounds. 
            ## We examine the modulus of the search value to keep things odd when i==1 and even when i==0
            ##########################################################################################################################
            x = start + (end - start)/2
            x += i - (x%2)
            
    

def find_end(population):

    ##########################################################################################################################
    ##  We cannot reliably say that R(n) > n: examples include R(5) = 4 and R(7) = 6
    ##  
    ##  The goal here is to quickly find an upper bound to the possible n that generates a given population. We will examine
    ##  odd values (for reasons given in the populations function) and go up by a factor of 2 in loops to find a quick upper bound.
    ##  
    ##  We could have assumed that the upper bound is the incoming population or higher; but by coming from the bottom up
    ##  we take advantage of the population generally growing by a factor of 2 over n, and therefore keeping our range of n
    ##  as small as possible.
    ##########################################################################################################################
    
    # start with the highest odd value in the populations dictionary
    x = max(populations) + (max(populations) % 2) + 1

    while True:
        result = R(x)
        
        if result >= population:
            return x
        elif result < population:
            x = (x*2) + 1
       
            
def R(n):

    ##########################################################################################################################
    ##  Per the problem, this recursive function returns the population of zombits at a given input time.
    ##  We check the global populations dictionary to speed up the process.
    ##########################################################################################################################
    if not n in populations:    

        if n % 2 == 0:
            x = n/2
            populations[n] = R(x) + R(x + 1) + x

        else:
            x = (n - 1)/2
            populations[n] =  R(x - 1) + R(x) + 1
    
    return populations[n]