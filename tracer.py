# A program that may be used to assist with debugging Python programs.
# Lehlogonolo Tshehla
# 15 May 2025

import os.path
print("***** Program Trace Utility *****")
filename = input("Enter the name of the program file: ")
file = open(filename,"r")
text = file.readlines()

def  isDebug(text):
    for lines in text:
        lines = lines.strip()
        if lines == '"""DEBUG"""' or lines == ('    """DEBUG""";print(\''):
            return True
        else:
            return False
def tracer(text):
    new_text = []
    func_name = []
    if isDebug(text) == True:
        print("Program contains trace statements")
        print("Removing...",end="")
        for lines in text:
            if '"""DEBUG"""' not in lines or ('    """DEBUG""";print(\'') not in lines:
                new_text.append(lines)
        del new_text[0]
        return new_text
    else:
        print("Program doesn't contains trace statements")
        print("Inserting...",end="")
        text.insert(0,'"""DEBUG"""\n')
        for lines in text:
            if "def" in lines:
                new_text.append(lines)
            
        for lines in text:
            fnc = " "
            func= " "
            if "def" in lines:        
                z = lines.index("def")  
                x = lines.index("(")
                fnc = lines[z+4:x]
            if fnc != " ":
                func = fnc
                func_name.append(func)
                f_names = f'    """DEBUG""";print(\'{func}\')'
        for r in range(len(text)):
            if text[r] in new_text:
                for f in range(len(func_name)):
                    if func_name[f] in text[r]:
                        text.insert(r+1,f'    """DEBUG""";print(\'{func_name[f]}\')\n')
        return text    

newfile = open(filename,"w")
new_text = tracer(text)
for lines in new_text:
    temp = str(lines)
    newfile.writelines(temp)
print("Done")
file.close()
newfile.close()
  