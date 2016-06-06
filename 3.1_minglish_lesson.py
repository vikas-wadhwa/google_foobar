##########################################################################################################################
##  Google foobar - 3.1 - minglish_lesson.py
##
##  Created by Vikas Wadhwa  http://www.wadhwa-media.com
##########################################################################################################################
    
##########################################################################################################################
## INSTRUCTIONS
#
# Minglish lesson
# ===============
# 
# Welcome to the lab, minion. Henceforth you shall do the bidding of Professor Boolean. Some say he's mad, trying to develop a zombie serum and all... but we think he's brilliant! 
# 
# First things first - Minions don't speak English, we speak Minglish. Use the Minglish dictionary to learn! The first thing you'll learn is how to use the dictionary.
# 
# Open the dictionary. Read the page numbers, figure out which pages come before others. You recognize the same letters used in English, but the order of letters is completely different in Minglish than English (a < b < c < ...).
# 
# Given a sorted list of dictionary words (you know they are sorted because you can read the page numbers), can you find the alphabetical order of the Minglish alphabet? For example, if the words were ["z", "yx", "yz"] the alphabetical order would be "xzy," which means x < z < y. The first two words tell you that z < y, and the last two words tell you that x < z.
# 
# Write a function answer(words) which, given a list of words sorted alphabetically in the Minglish alphabet, outputs a string that contains each letter present in the list of words exactly once; the order of the letters in the output must follow the order of letters in the Minglish alphabet. 
# 
# The list will contain at least 1 and no more than 50 words, and each word will consist of at least 1 and no more than 50 lowercase letters [a-z]. It is guaranteed that a total ordering can be developed from the input provided (i.e. given any two distinct letters, you can tell which is greater), and so the answer will exist and be unique.
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
#     (string list) words = ["y", "z", "xy"]
# Output:
#     (string) "yzx"
# 
# Inputs:
#     (string list) words = ["ba", "ab", "cb"]
# Output:
#     (string) "bac"
##########################################################################################################################


def answer(words):
        
    #test case input: ["ba", "ab", "cb"]
    # words = ["z", "yx", "yz"]
    
    ##########################################################################################################################
    ##  We can generate arrays of known alphabetical order, based on the first n characters each word shares.
    ##  so that ["z", "yx", "yz"] would yield 
    ##  1.  an array of [z,y] when looking at the first character of each word,
    ##  2.  two arrays z[''] and y[x,z] when we list the first characters that appears after grouping by the 1st character
    ##     
    ##  we then take the results, [z,y] and [x,z],  and compute the ordering to generate [x,z,y]
    ##########################################################################################################################
    
    alphabet = set()
    dictionaries = {}
    max_word_length = len(max(words, key=len))
    results = []
    

    ##########################################################################################################################
    ##  We here analyze the first character after a given character group, starting with the very first letter of each input word
    ##  and then the first characters of each word that starts with the same group (i.e. ape and apple both start with 'ap')
    ##
    ##  This will generate a hash of 'dictionaries' that holds a series of arrays, each one logically in order, grouped by a
    ##  key that was the first group of letters the characters in that list shared when found in the input words
    ##########################################################################################################################
    for group_length in range(0, max_word_length):
    
        
        # create a temp collection so we're not forced to remove items trivial conclusions from the result set
        collection = {}
        
        
        for word in words:                  
            
            if len(word) > group_length:
                # since this word is longer than group length, create a key, 
                # based on the characters up to group_length, in our temporary collection
                collection.setdefault(word[:group_length], [])
                
                # find the first character after the initial group length. Only add if it is a distinctly new character 
                # to the group's list
                if word[group_length:group_length+1] not in collection[word[:group_length]]:
                    collection[word[:group_length]].append(word[group_length:group_length+1])
                    alphabet.add(word[group_length:group_length+1])
        
        
        # only add elements to the dictionaries if the group has a list of more than 1 element, 
        # otherwise it gives us no true indication of order
        for group_sequence, characters_list in collection.iteritems():
            
            if len(characters_list)>1:
                dictionaries[group_sequence] = characters_list
    

    ##########################################################################################################################
    ##  We now loop through the found set of letters in the alphabet, and find it's index in each of the ordered dictionary lists.
    ##  
    ##  The first character of our real alphabet will ALWAYS appear at index 0.
    ##
    ##  The next loop will remove the known first letter from search of the next letter, so that the next letter that
    ##  ALWAYS has index 0 must now be the second letter, and so on, removing and repeating the search.
    ##########################################################################################################################
    
    while len(results) < len(alphabet) :
    
        for letter in alphabet :
    
            placements = set()
            
            for d in dictionaries.values():
            
                for found in results:
                    if found in d: d.remove(found)
                
                if letter in d: placements.add(d.index(letter))
                    
            if 0 in placements and len(placements) == 1 :
                results.append(letter)
                

    return ''.join(results)





