# A program  that asks the user to enter a word length and a filename. The program will search the ‘EnglishWords.txt’ file (of question 1) for sets of word that are that length and are anagrams of each other, and will write the results to a file with the given filename.
# Lehlogonolo Tshehla
#15 May 2025

print("***** Anagram Set Search *****")
import os.path

if os.path.isfile("EnglishWords.txt"):
    word_len = int(input("Enter a word length:\n"))
    filename = input("Enter file name:\n")
    print("Writing results...")
    file = open("EnglishWords.txt","r")
    text = file.read()
    file.close()
    
    
    start = text.find("START")
    text = text[start+5:]
    words = []
    words = text.split("\n")
    
    s_size = []
    for size in words:
        if len(size) == word_len :
            s_size.append(size)
    
    couple = []
    for w in s_size:
        bank1 = {}
        temp = []
        for lett in w:
            if lett not in bank1:
                bank1[lett] = 1
            else:
                bank1[lett] += 1
        for r in range(1,len(s_size)):
            test_w = s_size[r]
            bank2 = {}
            for lett in test_w:
                if lett not in bank2:
                    bank2[lett] = 1
                else:
                    bank2[lett] += 1
            if bank1 == bank2 and w != test_w:
                temp.append(w)
                temp.append(test_w)
        if len(temp) != 0:
            couple.append(temp)
            couple.sort()
    anagrams = []
    for ar in couple:
        ar.sort()
        if ar not in anagrams:
            anagrams.append(ar)
    
    newFile = open(filename,"w")    
    for ana in anagrams:
        temp = str(ana)
        newFile.writelines(temp)
        newFile.writelines("\n")
    newFile.close()