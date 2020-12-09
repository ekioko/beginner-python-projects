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

left_right = input("You are at a crossroads, which way would you like to go? Left or right? ").lower()

if left_right == "left":
  swim_wait = input("You go left and come across a lake. There is an island in the lake. Do you want to wait for a ferry across or try and swim? Type wait or swim. ").lower()
  if swim_wait == "wait":
    door = input("You wait a few hours for a ferry and are safely taken across to the island. The island has three doors, one blue, one red, one yellow. Which door would you like to open? Type red, blue, or yellow. ").lower()
    if door == "yellow":
      print("Congrats, you found the treasure! You win.")
    elif door == "red":
      print("You open the door, creep in a few feet and are consumed by a raging fire. You lose.")
    elif door == "blue":
      print("The door flies open and you are eaten within moments by a dozen beasts. You lose.")
    else:
      print("Game over.")
  else:
    print("You attempt to swim across but are attacked and eaten by viscious trout. Game over.")
else:
  print("You fell into a hole. Game over.")
