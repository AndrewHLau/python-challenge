# Dependencies
import os
import csv

with open('../Resources/election_data.csv') as file_:
	reader = csv.reader(file_)

	header = next(reader)
	prev_row = next(reader)
	reader = list(reader)
    #The total number of votes from the data
	totalvotes = 1

#A complete list of candidates who received votes
#The percentage of votes each candidate won, 
#count the number of votes each candidate received

	candidatevotes = {}

	for row in reader:
		#For total number of votes
		totalvotes = totalvotes+1
		try:
			candidatevotes [row[2]]+=1
		except:
			candidatevotes [row[2]]=1

print("Election Results")
print("----------------------------------")
print ("Total Votes:",totalvotes)
print ("--------------------------------")

#The winner of the election based on popular vote
#Print the candidate that received the most votes
best = ["",0]

for key,value in candidatevotes.items():
	if value > best[1]:
			best[1]=value
			best[0]=key
	print(f"{key}: {value/totalvotes} {value}")

print ("--------------------------------")
print (f"Winner: {best[0]}")
print ("--------------------------------")

output = (
	f"Election Results\n"
	"----------------------------------\n"
	f"Total Votes: {totalvotes}\n"
	"----------------------------------\n"
	f"{key}: {value/totalvotes} {value}\n"
	"----------------------------------\n"
	f"Winner: {best[0]}\n"
	"----------------------------------\n"
	)

# Specify the file to write to
output_path = os.path.join("..", "output", "election.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
	csvfile.write(output)