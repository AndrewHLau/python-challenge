# Dependencies
import os
import csv


# Store the file path associated with the file (note the backslash may be OS specific)
file = '../Resources/budget_data.csv'

print("Financial Analysis")
print("----------------------------------")

#The total number of months included in the data set
#Count the number of lines

print ("Total Months:")

#The net total amount of profit/Losses over the entire period
#sum the profits
print ("Total:")

#The average of the changes in Profit/Losses over the entire period

#mean the profits
print ("Average Change:")


#The greatest increase in profits (date and amount) over the entire period
print ("Greatest Increase in Profits:")


#The greatest decrease in losses (date and amount) over the entire period
print ("Greatest Decrease in Profits:")

# Specify the file to write to
output_path = os.path.join("..", "output", "new.csv")
