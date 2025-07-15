# A program  that searches a file for anagrams of a given word, printing the results in alphabetical order
# Lehlogonolo Tshehla
# 13 May 2025

print("***** Anagram Finder *****")
import os.path

if os.path.isfile("EnglishWords.txt"):
    word = input("Enter a word:\n")
    word = word.lower()
    file = open("EnglishWords.txt","r")
    text = file.read()
    file.close()
    
    
    start = text.find("START")
    text = text[start+5:]
    words = []
    words = text.split("\n")
    
    bank1 = {}
    same = []
    
    for lett in word:
        if lett not in bank1:
            bank1[lett] = 1
        else:
            bank1[lett] += 1    
    
    
    for w in words:
        bank2 = {}
        
        if len(word) == len(w):
            for lett in w:
                if lett not in bank2:
                    bank2[lett] = 1
                else:
                    bank2[lett] += 1            
            if bank1 == bank2 and w != word:
                same.append(w) 
    if len(same) != 0:
        print(same)
    else:
        print(f"Sorry, anagrams of '{word}' could not be found.")

else:
    print("Sorry, could not find file 'EnglishWords.txt'.")

