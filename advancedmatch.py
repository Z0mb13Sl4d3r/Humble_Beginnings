# A program that can be used to determine if a given pattern matches a given word
# Lehlogonolo Tshehla
# 30 April 2025

def match(pattern, word,i=0):
    if word == "" and pattern == "*":
        return True
    if (pattern and word) == '':
        return 
    
    if (pattern or word) == '':
        return
    
    if pattern == 'q':
        return 
    
    if (len(word) and len (pattern)) == 1:
        return True
    
    x = pattern.find("*")
    
    if len(word) != len(pattern):
        piece = pattern[:x]+pattern[x+1:]
        p = piece[0]
        pp = piece[1]
        if p in word and pp in word:
            return True
    else:
        if (pattern[i] == "?" and word[i].isalpha()) or (pattern[i] == word[i]):
            return match(pattern[i+1:], word[i+1:])
        else:
            piece = pattern[:x]+pattern[x+1:]
            q = piece.find("?")
            if "?" in piece:
                return match(pattern[i+1:], word[i+1:])        
            else:
                y = piece.find("*")
                if y > 0:
                    piece2 = piece[:y]+piece[y+1:] 
                    print(piece2)
                    pp = piece2[0]
                    if pp in word:
                        return True
                    else:   
                        return False


def main():
    pattern = input("Enter a pattern (or 'q' to quit):\n")
    word = input("Enter a word:\n")
    match(pattern, word)
    
if __name__ == "__main__":
    main() 