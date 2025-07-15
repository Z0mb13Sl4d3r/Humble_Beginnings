# A program that can be used to determine if a given pattern matches a given word
# Lehlogonolo Tshehla
# 30 April 2025

def match(pattern, word,i=0):
    if (pattern and word) == '':
        return 
    
    if (pattern or word) == '':
        return
    
    if pattern == 'q':
        return 
    
    if (len(word) and len (pattern)) == 1 and (word == pattern):
        return True
    
    if (len(word) and len (pattern)) == 1 and (pattern[i] == "?" and word[i].isalpha()):
        return True
    
    if len(pattern) == len(word):
        if (pattern[i] == "?" and word[i].isalpha()) or (pattern[i] == word[i]):
            return match(pattern[i+1:], word[i+1:])
        else:
            return False
    else:
        return False   
    
def main():
    pattern = input("Enter a pattern (or 'q' to quit):\n")
    word = input("Enter a word:\n")
    print(match(pattern, word))
    
if __name__ == "__main__":
    main()
