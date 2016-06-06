##########################################################################################################################
##  Google foobar - 3.3 - string_cleaning.py
##
##  Created by Vikas Wadhwa  http://www.wadhwa-media.com
##########################################################################################################################

##########################################################################################################################
## INSTRUCTIONS
#
# String cleaning
# ===============
# 
# Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who are turning rabbits into zombies. He sends a text transmission to you, but it is intercepted by a pirate, who jumbles the message by repeatedly inserting the same word into the text some number of times. At each step, he might have inserted the word anywhere, including at the beginning or end, or even into a copy of the word he inserted in a previous step. By offering the pirate a dubloon, you get him to tell you what that word was. A few bottles of rum later, he also tells you that the original text was the shortest possible string formed by repeated removals of that word, and that the text was actually the lexicographically earliest string from all the possible shortest candidates. Using this information, can you work out what message your spy originally sent?
# 
# For example, if the final chunk of text was "lolol," and the inserted word was "lol," the shortest possible strings are "ol" (remove "lol" from the beginning) and "lo" (remove "lol" from the end). The original text therefore must have been "lo," the lexicographically earliest string.
# 
# Write a function called answer(chunk, word) that returns the shortest, lexicographically earliest string that can be formed by removing occurrences of word from chunk. Keep in mind that the occurrences may be nested, and that removing one occurrence might result in another. For example, removing "ab" from "aabb" results in another "ab" that was not originally present. Also keep in mind that your spy's original message might have been an empty string.
# 
# chunk and word will only consist of lowercase letters [a-z].
# chunk will have no more than 20 characters.
# word will have at least one character, and no more than the number of characters in chunk.
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
#     (string) chunk = "lololololo"
#     (string) word = "lol"
# Output:
#     (string) "looo"
# 
# Inputs:
#     (string) chunk = "goodgooogoogfogoood"
#     (string) word = "goo"
# Output:
#     (string) "dogfood"
##########################################################################################################################

    

def answer(chunk, word):

    found_indices = []
    overlapping_indices = []
    
    
    
    ##########################################################################################################################
    ##  Our approach will be to analyze the incoming string and, if no words in the chunk overlap each other, simple remove all
    ##  remove all instances of the word.
    ##  
    ##  If there is an instance of overlapping, we will loop through each possibility, recursively removing words further if
    ##  since new ones may have been formed. We keep track of the results and if a new final result is smaller, or of equal size
    ##  and lexicographically first, we use that as the new final result.
    ##########################################################################################################################
    if word in chunk: 
    
        # find all instances of the word, storing if there are any overlaps
        for i in range(0, len(chunk) - len(word)+1):
            if chunk[i:i+len(word)] == word:
                if len(found_indices) > 0 and found_indices[-1] >= i - len(word) + 1:
                    overlapping_indices.append(found_indices[-1])
                    overlapping_indices.append(i)
                found_indices.append(i)

        # if no overlaps, simply remove all instances of the word and return the result
        if not overlapping_indices:
            cleaning = chunk.split(word)
            cleaning = ''.join(cleaning)
            cleaned = answer(cleaning, word)
            return cleaned

        # if there are overlaps, check the possibilities of results against the removal of each one
        else: 
            result = chunk
            
            for index in overlapping_indices:
                cleaning = chunk[0:index] + chunk[index+len(word):]
                cleaned = answer(cleaning, word)
                            
                if len(cleaned) < len(result) or (len(cleaned) == len(result) and cleaned < result):
                    result = cleaned
                
            return result
        
    # because we are recursing, if we get to the point where the word is completely removed, return the starting point
    else:
        return chunk