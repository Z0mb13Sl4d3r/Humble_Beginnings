# A program that takes a users sentence and a word to find then indicates whether the word is in the sentence and what index does it first appears
# Lehlogonolo Tshehla
# 07 April 2025

sentence = input("Enter a sentence:\n") # this asks for the sentence in which we will look for a particular word

word = input("Enter the word to find:\n") # this will be the word we will look from the given sentence

word = word.lower()

words = [] # this array will contain the all the individual words in the sentence

sent = "" # this will be the variable which we will use to build up the word we want

temp = [] # this is the temporary list which will store each word built

for i in sentence:
    
    if i != " " and i != "." and i != "," and i != "!" and i != "?" and i != ";" and i != ":":
    
        sent += i # this loop will take each indiviual character of the string then build it into a word then stops when there is a space or etc.
    
    else: 
    
        temp += [sent] # when a space is encountered, then we take our built word and put it into an arrray to be stored
    
        for a in temp: 
    
            if a != "":
    
                words += [a] # this will take the word made in the temporary array and place it into our array that will contain all the properly formed words
    
        temp = [] # lines 31 and 33 are there to reset our word and start a new word from the string given by the user
    
        sent = ''

count = 0 # this will keep track of all the words in the array

for x in words:
    
    if x.lower() == word: # we are looking if the word the user wants to find is in the array of words from the sentence given by the user
    
        print(f"The word '{word}' is in the sentence.")
        counter = 0
        first = word[0]
        
        for x in sentence:
            if x.lower() != first:
                counter += 1
            else:
                print(f"It first appears at index {counter}.")
                break        
    
        break # once the word is discovered to be in the string, we immediately break the whole for loop and are left with the result
    
    else:
    
        count += 1 # this will increase until we either find the word the user wants or we have gone through all the elements in our array
    
        if count == len(words): # if the value of count matches the number of elements in the array, then we have not found the word and it is not in the given sentence.
    
            print(f"The word '{word}' is NOT in the sentence.")


# The Quick Brown Fox Jumped Over The Lazy Dog 