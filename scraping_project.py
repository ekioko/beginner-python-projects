import requests
from bs4 import BeautifulSoup
from csv import writer,reader
# import random
# import tkinter as tk


response = requests.get("http://quotes.toscrape.com/") # make request to http://quotes.toscrape.com/
soup = BeautifulSoup(response.text, "html.parser") # import to beautiful soup

with open("quote_game.csv", "w") as csv_file: # write data to csv
	csv_writer = writer(csv_file)
	csv_writer.writerow(["Quote", "Author", "Url"])
	nxt_pg = 0
	# if next button is present,
	# go to next page 
	while nxt_pg <= 10:
		for quote in soup.select(".quote"):
			q_tag = quote.find(class_= "text")
			current_quote = q_tag.get_text() # grab quote
			author_tag = quote.find(class_="author")
			current_author = author_tag.get_text() # name of author
			# print(current_author)
			url_tag = quote.find("a")["href"] # url (href) to biographical data for in-game prompts
			url = "http://quotes.toscrape.com" + url_tag
			csv_writer.writerow([current_quote, current_author, str(url) + "/"])
		nxt_pg += 1
		response = requests.get("http://quotes.toscrape.com/page/" + str(nxt_pg) + "/")
		soup = BeautifulSoup(response.text, "html.parser") # import to beautiful soup


		# grab author bios
with open("quote_game_authors.csv", "w") as csv_file: # create new csv for bio data
	csv_writer = writer(csv_file)
	csv_writer.writerow(["First Initial", "Last Initial", "Biographical Info"])

	with open("quote_game.csv") as file: # run through each row of main csv to grab urls
		csv_reader = reader(file)
		next(csv_reader)
	    
		for row in csv_reader:
			url = row[2]
			print(url)
			response = requests.get(url)
			soup = BeautifulSoup(response.text, "html.parser")
			hints = soup.select(".author-details")[0]
			a_tag = hints.find(class_="author-title")
			current_author = a_tag.get_text()
			year_tag = soup.find(class_= "author-born-date")
			year = year_tag.get_text()
			place_tag = soup.find(class_= "author-born-location")
			place = place_tag.get_text()
			bio_hint = "This person was born " + str(year) + " " + str(place)
			a_hints = current_author.split()
			first_initial = a_hints[0][0]
			last_initial = a_hints[-1][0]
			csv_writer.writerow([first_initial, last_initial, bio_hint])

            # biographical data
			#csv_writer.writerow([])




		# first initial
		# last initial
		# biographical data




# #game logic



# # game play: display quote to user
# # display number of guesses remaining
# # if answer incorrect, provide hint
# # first hint is biographical data (place born and date)
# # second guess
# # decrement guesses remaining
# choose_quote()





#################################################
# widget code

# create buttons and user input window

# window = tk.Tk()
# window.title("Quote Guessing Game")

# lblInst = tk.Label(window, text = chosen_row) #DISPLAY CHOSEN QUOTE HERE
# lblLine0 = tk.Label(window, text= "*********************************************************************")
# lblNoGuess = tk.Label(window, text= "No of Guesses: 0")
# lblMaxGuess = tk.Label(window, text= "Max Guess: 4")
# lblLine1 = tk.Label(window, text= "*********************************************************************")
# lblLogs = tk.Label(window, text="Game Logs")
# lblLine2 = tk.Label(window, text= "*********************************************************************")


# # append elements to grid
# lblInst.grid(row=0, column=0, columnspan=5)
# lblLine0.grid(row=1, column=0, columnspan=5)
# lblNoGuess.grid(row=2, column=0, columnspan=3)
# lblMaxGuess.grid(row=2, column=3, columnspan=2)
# lblLine1.grid(row=3, column=0, columnspan=5)
# lblLogs.grid(row=4, column=0, columnspan=5)  # row 4 - 8 is reserved for showing logs
# lblLine2.grid(row=9, column=0, columnspan=5)

# window.mainloop()
