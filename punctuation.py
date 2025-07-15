# A program that removes all punctuation marks (.,!?;:) from a paragraph it also counts and displays the number of unique words in a paragraph
# Lehlogonolo Tshehla
# 02 April 2025

paragraph = input("Enter a paragraph of any length:\n") # this asks for input from the user for the paragraph
  
para_array = [] # this is the empty set that will be used to give the number of words and what those words are

print("A paragraph without punctuation:")

for p in paragraph: # this for loop will give out a sentence that does not have any punctuation inside it
    if p == ".": # from lines 12 to 23, these remove the punctuation from the sentence if there is any punctuation
        continue
    if p == ",":
        continue
    if p == "!":
        continue
    if p == "?":
        continue
    if p == ";":
        continue
    if p == ":":
        continue
    if p == "-":
        continue
    print(p,end="") # this prints out the sentence without any punctuation

print("")
para = "" # this is the variable that'll be used to join the characters of the string together to form words
array = [] # this is the array that will store the words and will be used to extract the words from
for i in paragraph:
    if i != " " and i != "." and i != "," and i != "!" and i != "?" and i != ";" and i != ":" : # this is to avoid the punctuations in the "paragraph" string
        para += i # this will continue until a a whitespace is hit and a word is formed
    else: # when a whitespace is hit, the code will execute this else statement
        array += [para] # this stores the created word into the list called array
        for a in array: # this loop takes the elements in the list called arrays and joins it into the list called para_array
            if a != "":
                para_array += [a] # this is the form that works as the inbuilt function called append
        array = [] # lines 37 and 38 are there so that a new word is formed
        para = ''

para = {}
array = []
for n in para_array: # this for loop iterates through the list of user input and uses them as keys to be put into a dictionary
    if n in para:
        para[n] += 1 # this adds 1 to any number that is already a key in the dictionary created
    else:
        para[n] = 1 # this assigns the value 1 to any new keys in the dictionary
        
for keys in para.keys(): # this is how we get a array of all the numbers from the user without any duplications
    array.append(keys)
        
print("The number of unique words in a paragraph:")
print(len(array))
print("The unique words are:")
print(array)
