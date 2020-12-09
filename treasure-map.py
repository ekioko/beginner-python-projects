row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

#user inputs coordinates as one number (e.g., 2X3 = '23')
position = input("Where do you want to put the treasure? ")

co_ord = []
for char in position:
  co_ord.append(char)

across = int(co_ord[0])-1
down = int(co_ord[1])-1
map[across][down] = 'X'

print(f"{row1}\n{row2}\n{row3}")
