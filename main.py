print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

name = input("Choose your nickname: ").capitalize()

print("Welcome to your adventure, ", name, "!")

user_path = input("Choose a path for your adventure, rocky or muddy? type rocky to start your adventure on rocky "
                  "grounds or type muddy to start on muddy ground: ").lower()

if user_path == "rocky":
    print("Tighten your boots and off you go.")
    answer = input("You have now reached the lion's den, choose "
                   "to go left or right, your option may keep you alive! ").lower()
    if answer == "left":
        print("Aaahhhh, you just got eaten by the lion, you lose!")
    elif answer == "right":
        print("You have been bitten by the lion, you lose!")
    else:
        print("Not a valid option!, you lose")

elif user_path == "muddy":
    print("Roll-up your sleeves, it's gonna get dirty! off you go.")
    answer = input("You have arrived the alligator's den, choose left or right to stay alive: ").lower()
    if answer == "left":
        print("You have now escaped the lion and standing near a bridge leading up to the sea, "
              "your next choice of action may keep you alive or kill you.")
        answer = input("Choose left or right: ").lower()
    if answer == "left":
        print("You made it to the sea safely!")
        answer = input("You come across a stranger at the sea, do you talk "
                       "to them or ignore them? (yes/no): ").lower()
        if answer == "yes":
            print("The stranger likes you and gifts you a tonne of gold, you win!")
        elif answer == "No":
            print("The stranger is angry that you ignored them and drowns you in the sea, you lose!")
        else:
            print("Not a valid option")
    elif answer == "right":
        print("You fell off the bridge and died, you lose.")
    else:
        print("Not a valid option, you lose.")
else:
    print("Invalid option!, you lost")

print("Thank you for trying", name, ".")

