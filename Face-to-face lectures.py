#x=2
#if x>2:
   #print("Greater")
#else:
   #print("Less than")

#alibi = input("Do you have an alibi?\n")
#motive = input("Do you have a motive?\n")
#record = input("Do you have a criminal record?\n")

#alibi_var = alibi=="yes" or alibi=="Yes" or alibi=="Y" or alibi=="y"
#motive_var = motive=="yes" or motive=="Yes" or motive=="Y" or "y"
#record_var = record=="yes" or record=="Yes" or record=="Y" or record=="y"

#if alibi_var:
   #print("They are innocent")
#elif motive_var or record_var:
   #print("100% guilty")

#x = [1, 2, 3, 4, 5, 6]

#for i in range(10):
    #print(i,end=" ")
#print (" ")
#for i in range(0,10,2):
    #print(i,end=" ")
#print(" ")
#for i in range(-1,-10,-2):
    #print(i,end=" ")
#print(" ")
#word = "CSC1015F"
#for ch in word:
    #print(ch,end=" ")
#print(" ")
#n = 0
#while n<10 :
    #print(n,end=" ")
    #n +=1
#print(" ")

#w = 0
#while w<100:
    #print(w,end=" ")
    #w +=7

####while n>1:
   ####print("I'm in a loop!!",end=" ",sep="@")
#print("")
#user = input("Put in a string: \n")
#data = []
#while len(data)<5:
   #data.append(user)
   #user = input("Put in a string\n")

#print(len(data))
#print(data)

#set_list = []
#new_list = []
#print("Enter a set of numbers to do a prefix sum:")
#while set_list != " ":
   #var = int(input(""))
   #set_list.append(var)
   #if var == " ":
       #break
#sum = 0
#for x in set_list:
   #sum +=x
   #new_list.append(sum)
#print(new_list)

#print(25%5==5)
#x = 5
#if x<5:
    #print("True")
#else:
    #print("False")

#word = "TRADE"
#guess = input("Guess the 5 letter word:\n ")
#guess = guess.upper()
#output = ""
#for i in range(len(guess)):
    #if guess[i] == word[i]:
        #output += "*"
    #elif guess[i] in word:
        #output += "+"
    #else:
        #output += "-"
#print("["+output+"]")

#from math import pi

#x = 1
#x = 1*pi
#print("The value of pi is: %.2f." % x)
##
#def your_birth(age):
    #current = 2025
    #how_old = 2025 - age
    #return how_old

#def main():
    #print()
    #age = int(input("What is your age?\n"))
    #born = your_birth(age)
    #print(f"You are born on {born}.")



#if __name__=="__main__":
    #main()

#v = 515
#x = v//100
#y = (v-x*100)//10


#print(x,y)

#def countdown(n):
    #if n==0:
        #print("Lift off")
        #return
    #else:
        #print(n)
        #countdown(n-1)

#countdown(10)

#def add(n):
    #if n==0:
        #return 0
    #else:
        #return n+add(n-1)

#print("The sum is",add(10))

#def fact(n):
    #if n == 0:
        #return 1
    #else:
        #return n * fact(n-1)
    
#print("The factorial of that number is",fact(5))

# f1 = open("article.txt","r")
# reads = f1.read()
# print(reads,end="")
# f1.close()

# f2 = open("article.txt","r")
# whole = f2.readline()
# print(whole,end="")
# f2.close()

# f3 = open("article.txt","r")
# list = f3.readlines()
# print(list,end="")
# f3.close()

# f4 = open("article.txt","r")
# i = 1
# for l in f4:
#     print(i,l,end="")
#     i += 1
# f4.close()

# wr = open("article.txt","a")
# print("we added stuff into this file\n","type type brah\n",article=wr)

# def binary (value,target,start,stop):
#     if start > stop:
#         return -1
#     middle = (start-stop)//2
#
#     if value[middle] < target:
#         return binary(value,target,middle+1,stop)
#     return binary(value,target,start,middle-1)
#
# def main():
#     value = input("Give a word to search:\n")
#     list = [34, 12, 17, 34, 55, 48, 20, 23, 55, 19, 35, 65, 9, 84]
#     list = list.sort()

