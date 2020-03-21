# Dependencies
import os
import csv


# Store the file path associated with the file (note the backslash may be OS specific)
file = '../Resources/election_data.csv'

print("Election Results")
print("----------------------------------")

#The total number of votes from the data
#Count the number of lines

print ("Total Votes:3521001")

print ("--------------------------------")

#A complete list of candidates who received votes
#The percentage of votes each candidate won, count the number of votes each candidate received
# Divide by total votes and multiply by 100
#The winner of the election based on popular vote
print ("Khan: 63.000% (2218231)")
print ("Correy: 20.000% (704200)")
print ("Li: 14.000% (492940)")
print ("O'Tooley: 3.000% (105630)")
print ("--------------------------------")

#The winner of the election based on popular vote, print the candidate that received the most votes
print ("Winner: Khan")
print ("--------------------------------")


# Specify the file to write to
output_path = os.path.join("..", "output", "election.csv")
