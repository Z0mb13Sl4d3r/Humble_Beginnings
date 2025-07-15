# Given a word, calculate how many syllables it contains.
# Lehlogonolo Tshehla
# 14 April 2025

def count_syllables(word):
    count = 0
    vowels = ['y','a', 'e', 'i', 'o', 'u']
    temp = word
    x = 0
    
    while word != "q":
        if word == "q":
            break
        for w in word:
            x = temp.find(w)
            if len(word) == 1 and w in vowels :
                count = 1
                break
            if len(word) <= 2 and ( w == "e" or word[-1] == "e" ):
                count = 1
                break
            
            if len(word) >= 2 and w == "e":
                count += 1 
                break                
            if len(word) >= 2 and word[-1] == "e":
                count = 1 
            if len(word) >= 2 and w == "e":
                count = 1   
            if  len(word) >= 2 and w in vowels :
                count += 1                
                if (word[x] and word[x-1]) in vowels:
                    count -= 1
                    break
                if len(word) >= 2 and w == "e" and not(word[x-1] in vowels):
                    count = 1
                    break                
        return count
                    
    
def main():
    word = input("Enter a word (or 'q' to quit):\n")
    if word != "q":
        if count_syllables(word) != " " and count_syllables(word) == 1:
            print(f"The word \'{word}\' has {count_syllables(word)} syllable.")
            print(" ")
        if count_syllables(word) != " " and count_syllables(word) >= 2:
            print(f"The word \'{word}\' has {count_syllables(word)} syllables.")
            print(" ")
        
        while word != "q":
            word = input("Enter a word (or 'q' to quit):\n")
            if word != "q":
                if count_syllables(word) != " " and count_syllables(word) == 1:
                    print(f"The word \'{word}\' has {count_syllables(word)} syllable.")
                    print(" ")
                if count_syllables(word) != " " and count_syllables(word) >= 2:
                    print(f"The word \'{word}\' has {count_syllables(word)} syllables.")
                    print(" ")
    else:
        while word != "q":
            word = input("Enter a word (or 'q' to quit):\n")
            if word != "q":
                if count_syllables(word) != " " and count_syllables(word) <= 1:
                    print(f"The word \'{word}\' has {count_syllables(word)} syllable.")
                    print(" ")
                if count_syllables(word) != " " and count_syllables(word) >= 2:
                    print(f"The word \'{word}\' has {count_syllables(word)} syllables.")        
                    print(" ")

if __name__ == '__main__':
    main()
