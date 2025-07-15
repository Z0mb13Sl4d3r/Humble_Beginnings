# A program that capitilizes the first letter of words and makes the author names in title case
# Lehlogonolo Tshehla
# 06 April 2025

ref = input("Enter the reference:\n")

formated = ref.capitalize() # this capitalizes the first ketter of the sentence

auth_e = formated.find("(")-1 # this will find the last letter  of the author in the reference before the start of the year

author = formated[:auth_e] # this will slice out the name of the author in the string
author = author.title() # this will capitalize the letters of the name and surname of the author

occu_s = formated.find(")")+2 # this will find the first letter of the word after the year in the reference

para = "" 
temp = []
pos = []
counter = 0
for i in ref:
    if i != "," :
        counter += 1 
    else: 
        temp += [counter] 
        for a in temp: 
            if a != "":
                pos += [a] 
        array = [] 
        para = ''
        
occu_e = pos[2]

occup = formated[occu_s:occu_e+1] # ths will slice the first word after the year but before the dash
occup = occup.capitalize() # this will capitaize the first letter if that word we have sliced out

print("Reformatted reference:")
print(author+ref[auth_e:occu_s]+occup+ref[occu_e+1:]) # this print will give the reformatted sentence that has the proper capitalzation

# poulo, lebeko bernard (2013) fine-grained scalability Of digital library services In The cloud, SAICSIT Conference 2014, ACM, pp23-34, 2014