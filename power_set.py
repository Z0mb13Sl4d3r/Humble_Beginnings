# A program that can be used to  find a power set
# Lehlogonolo Tshehla
# 30 April 2025

def sets(arr,i=-1):
    array = arr.split(" ")
    new = []
    if array == "":
        return []
    if new == []:
        new.append(array[i])
    if i < 0:
        
        if new[i] == array[i]:
            temp = array[i-1]
            new.append(temp)
            return new
        else:
            temp = array[i]
            new.append(temp)
            return sets(array,i-1)   

print(sets('3 2 5 4'))