##########################################################################################################################
##  Google foobar - 3.2 - spy_snippets.py
##
##  Created by Vikas Wadhwa  http://www.wadhwa-media.com
##########################################################################################################################

##########################################################################################################################
## INSTRUCTIONS
#
# Spy snippets
# ============
# You've been recruited by the team building Spy4Rabbits, a highly advanced search engine used to help fellow agents discover files and intel needed to continue the operations against Dr. Boolean's evil experiments. The team is known for recruiting only the brightest rabbit engineers, so there's no surprise they brought you on board. While you're elbow deep in some important encryption algorithm, a high-ranking rabbit official requests a nice aesthetic feature for the tool called "Snippet Search." While you really wanted to tell him how such a feature is a waste of time in this intense, fast-paced spy organization, you also wouldn't mind getting kudos from a leader. How hard could it be, anyway?
# 
# When someone makes a search, Spy4Rabbits shows the title of the page. Your commander would also like it to show a short snippet of the page containing the terms that were searched for.
#
# Write a function called answer(document, searchTerms) which returns the shortest snippet of the document, containing all of the given search terms. The search terms can appear in any order.
# 
# The length of a snippet is the number of words in the snippet. For example, the length of the snippet "tastiest color of carrot" is 4. (Who doesn't like a delicious snack!)
# 
# The document will be a string consisting only of lower-case letters [a-z] and spaces. Words in the string will be separated by a single space. A word could appear multiple times in the document.
# 
# searchTerms will be a list of words, each word comprised only of lower-case letters [a-z]. All the search terms will be distinct.
# 
# Search terms must match words exactly, so "hop" does not match "hopping".
# 
# Return the first sub-string if multiple sub-strings are shortest. For example, if the document is "world there hello hello where world" and the search terms are ["hello", "world"], you must return "world there hello". The document will be guaranteed to contain all the search terms.
#
# The number of words in the document will be at least one, will not exceed 500, and each word will be 1 to 10 letters long. Repeat words in the document are considered distinct for counting purposes.
#
# The number of words in searchTerms will be at least one, will not exceed 100, and each word will not be more than 10 letters long.
#
# Test cases
# ==========
# Inputs:
#     (string) document = "many google employees can program"
#     (string list) searchTerms = ["google", "program"]
# Output:
#     (string) "google employees can program"
# Inputs:
#     (string) document = "a b c d a"
#     (string list) searchTerms = ["a", "c", "d"]
# Output:
#     (string) "c d a"
##########################################################################################################################

import sys

def answer(document, searchTerms):
    ##########################################################################################################################
    # loop through and create a hash, with the key being each term 
    # and the value being an array of the index locations of that term within the document.
    # 
    # We use a FOR loop instead of an .index(term) because we need to find all occurrences, not just the first. Since we need
    # to loop through the string, best to do it once. We also keep track of 'frequency', or the number of times a search term
    # appears in the document. The least frequent is recorded for the second step.
    #
    # document: "a b c d a"
    # searchTerms: ["a", "c", "d"]
    # example: locations = { 'a': [0,4], 'c': [2], 'd': [3] }
    ##########################################################################################################################

    # set term_frequency to maxsize so we can keep looking for something lower
    # set least_frequent term to some existing value, we change when we find something verified as least frequent
    term_frequency = sys.maxsize
    least_frequent_term = searchTerms[0]
    indices = []
    locations = {}
         
    # turn document into an array of words, so we can determine apply some cardinality to the document
    words = document.split()

    for i, word in enumerate(words):    
        if word in searchTerms:         
            locations.setdefault(word, []).append(i)
            indices.append(i)

    for term in locations:
        if len(locations[term]) < term_frequency  and locations[term][0] < locations[least_frequent_term][0]:
            term_frequency = len(locations[term])
            least_frequent_term = term
    
    # remove any non-search terms on either end to shorten the array of words
    words = words[sorted(indices)[0]: sorted(indices)[-1] + 1]

    ##########################################################################################################################
    # Next, start with the minimum possible snippet length, which is the total number of search terms.
    # 
    # We see if all the terms exist within that length around the first least-frequent term in the document. We then go to any 
    # next instance of the same term and check there. If none are found for any of the instances of the given term,
    # we repeat and enlarge the search to one more word on either side.
    ##########################################################################################################################    
    results = []
     
    # search around the first least-frequent term
    for n, index in enumerate(locations[least_frequent_term]):        
        
        # we take half the searchTerm size since we want to search on either side of the least-frequent term
        min_snippet_length = int(len(searchTerms)/2)
        searching = True
        
        while searching:

            # search within a certain number of words on either side of the least-frequent term, a minimum value of int(len(searchTerms)/2)
            test_snippet = words[max(index - min_snippet_length, 0): index + min_snippet_length + 1]            
        
            # if all the terms are found within this length, this is the snippet we need                        
            if all(n in test_snippet for n in searchTerms):
            
                # if the snippet includes a non-search terms or repeated search terms on either end, shorten the snippet
                while 1:
                    if test_snippet[0] not in searchTerms or (test_snippet[0] in test_snippet[1:]): 
                        test_snippet = test_snippet[1:] 
                    else: break  
                
                while 1:
                    if test_snippet[-1] not in searchTerms or (test_snippet[-1] in test_snippet[:-1]) :
                        test_snippet = test_snippet[:-1]
                    else: break
                
                # this is the results snippet if it is shortest
                if n==0 or (n>0 and len(test_snippet) < len(results)):
                    results = test_snippet
                    
                searching = False

            min_snippet_length += 1   
    
    return ' '.join(results)

