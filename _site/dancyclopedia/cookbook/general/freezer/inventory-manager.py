## importing packages
import pandas as pd
from datetime import datetime

## Defining a class for managing the freezer inventory.
class inventory():

	## Initialising the class
	def __init__(self):
		super(inventory, self).__init__()
		## importing data frame from csv file
		self.freezer = pd.read_csv('./freezer.csv')
		self.addEntry()
		print(self.freezer)
		self.save = self.freezer.to_csv(r'./freezer.csv', index = None, header=True)


	## Function to add new entries to data frame.
	def addEntry(self):
		item = input("What are you freezing?: ")
		quantity = input("How many " + item + " should we log?: ")
		while quantity not in ["1", "2", "3", "4", "5"]:
			print("Please enter an integer number between 1 and 5.")
			quantity = input("How many " + item + " should we log?: ")
		note = input("Anything to note?: ")
		while "," in note:
			print("Please avoid using ',' punctuation.")
			note = input("Anything to note?: ")
		shelf = input("Where did you put it? Choose a shelf from 1 to 4: ")
		now = datetime.now() # take current date and time
		date = now.strftime("%d-%b-%Y") # format date to dd-Mon-yyyy
		code = now.strftime("%j-%M%S") # generate code based on day of the year, with minutes and seconds.
		newEntry = pd.Series([item, int(quantity), note, shelf, date, code], index=self.freezer.columns)
		self.freezer = self.freezer.append(newEntry, ignore_index=True)
		print(item + " added to the inventory.")

	## Function to remove entries.
	def removeEntry(self):
		pass

	## Function for the CLI.
	def interface(self):
		pass

## +++Run script+++
inventory()