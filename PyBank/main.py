# Dependencies
import os
import csv


# Store the file path associated with the file (note the backslash may be OS specific)
file = '../Resources/budget_data.csv'

print("Financial Analysis")
print("----------------------------------")

#The total number of months included in the data set
#Count the number of lines

print ("Total Months: 86")

#The net total amount of profit/Losses over the entire period
#sum the profits
print ("Total: $38382578")

#The average of the changes in Profit/Losses over the entire period

#mean the profits
print ("Average Change: $-2315.12")


#The greatest increase in profits (date and amount) over the entire period
print ("Greatest Increase in Profits: Feb-2012 ($1926159")


#The greatest decrease in losses (date and amount) over the entire period
print ("Greatest Decrease in Profits: Sep-2013 ($-2196167")

# Specify the file to write to
output_path = os.path.join("..", "output", "bank.csv")
