from math import trunc
import random
password = ["","","","","","","","","","","","","","","","","","","","","","","",""]
lowerCaseAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercaseAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
specialChars = ["@", "#", "$", "%", "&", "_", "?", "."]
numbers = ["1","2","3","4","5","6","7","8","9","0"]


def fillPW(fillEmptySpaces:bool, listName:list, forRange:list=0, forbiddenIndex:list=[]):
    global password
    
    if fillEmptySpaces == False: #Only executes this if it isnt supposed to fill all the empty spaces
        for i in range(0 ,random.randint(forRange[0] + 1, forRange[1] + 1)): #Determines the length of the type of characters added
            
            goFurther = False
            while goFurther == False: #Only continues if the index of the added number isnt a forbidden one and if its an empty space
                position = random.randint(1, 23) #Determines the index as for the position in the password
                if position in forbiddenIndex or password[position] != "": 
                    continue
                else:
                    goFurther = True
        
            charIndex = random.randint(0, len(listName) -1) #Determines the character of the characterlist that will be added   
            password[position] = listName[charIndex]#Adds the character at the index in the password

    else: #Executes this if it is supposed to fill all the empty spaces
        for i in range(len(password)):
            if password[i] == "":
                charIndex = random.randint(0, len(listName) -1)
                password[i] = listName[charIndex]



fillPW(False, uppercaseAlphabet, [2, 6]) #Uppercase Alphabet

fillPW(False, specialChars, [3, 3], [0, 23]) #Special characters

fillPW(False, numbers, [4, 7], [0, 1, 2]) #Numbers

emptySpaces = 0
for i in range(len(password)):
    if password[i] == "":
        emptySpaces += 1

fillPW(True, lowerCaseAlphabet, [emptySpaces, emptySpaces])

finalPw = ""
for i in range(len(password)):
    finalPw += password[i]

print(finalPw)