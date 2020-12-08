print("Welcome to the Tip Calculator!")

#ask user for bill total, number of people splitting bill, and tip percentage
total_bill = int(input("What was the total bill? "))
num_split = int(input("How many people are splitting the bill? "))
tip_percent = int(input("What percent would you like to tip? (e.g., 10, 12, 15...) "))

#calculate total amount
total_tip = total_bill + total_bill * (tip_percent / 100)

#format to second decimal point and divide by number of people splitting bill
total_split = "{:.2f}".format(total_tip/num_split)

print(f"Each person should pay ${total_split}.")
