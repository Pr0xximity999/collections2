import random
import time
stashedDice = []
rolledDice = []

def throw(num):
    dice = []
    for i in range(num):
        number = random.randint(1, 6)
        dice.append(number)
    return dice

for i in range(2):
    rolledDice = throw(5 - len(stashedDice))
    print("Uw dobbelstenen zijn:")
    for i in range(len(rolledDice)):
        print(f"nummer {i + 1} is een {rolledDice[i]}")
    
    proceed = False
    
    while proceed == False:
        takenNums = []
        takeDice = input("Wilt u een steen pakken? Y/N")
        if takeDice.lower() == "y": #If the user awnsered y on the question if he wanted to stash a dice
            while proceed == False:
                chosenDice = int(input("Welk nummer steen wilt u pakken? >>"))
                
                if chosenDice > len(rolledDice) or chosenDice <= 0: #If the number is higher than the amount of rolled dices
                    print("Dat nummer is geen keuze")

                elif chosenDice in takenNums: #If the user already has taken that number
                    print("Die steen heeft u al gepakt")

                else:
                    takenNums.append(chosenDice)
                    stashedDice.append(rolledDice[chosenDice - 1])

                    while True:
                        repeat = input("Wilt u nog een andere steen pakken? Y/N >>")
                        if repeat.lower() == "y":
                            break
                        elif repeat.lower() == "n":
                            proceed = True
                            break
                        else:
                            print("Dat is geen keuze, voer Y/N in")
                            continue
                        
        elif takeDice.lower() == "n":
            proceed = True
            break
        else:
            print("Dat is geen keuze, voer Y/N in")
            continue

while True:
    rolledDice = throw(5 - len(stashedDice))
    print("Uw dobbelstenen zijn:")
    for i in range(len(rolledDice)):
        print(f"{rolledDice[i]}")

    for i in range(len(stashedDice)):
        print(f"{stashedDice[i]}")

    print("Welke combinatie wil je maken?")
    time.sleep(0.25)
    print("three of a kind")
    time.sleep(0.25)
    print("four of a kind")
    time.sleep(0.25)
    print("full house")
    time.sleep(0.25)
    print("small straight")
    time.sleep(0.25)
    print("large straight")
    time.sleep(0.25)
    print("yahtzee")