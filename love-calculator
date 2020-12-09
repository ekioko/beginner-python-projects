print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

true = 0
love = 0

true_list = ["t","r","u","e"]
love_list = ["l","o","v","e"]

for char in true_list:
  true += name1.count(char)
  true += name2.count(char)
for char in love_list:
  love += name1.count(char)
  love += name2.count(char)

true_love = int(str(true) + str(love))

if true_love < 10 or true_love > 90:
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}.")
