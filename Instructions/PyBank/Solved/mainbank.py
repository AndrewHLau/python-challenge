
# Dependencies
import os
import csv


# Store the file path associated with the file (note the backslash may be OS specific)
with open('../Resources/budget_data.csv') as file_:
	reader = csv.reader(file_)

	header = next(reader)
	prev_row = next(reader)
	reader = list(reader)
	totalmonths = 1
	total = int(prev_row[1])
	total1 = int(reader[-1][1])-total
	total2 = 0
	#For the greatest increase 
	best = ["",-1000*1000]
	#For the greatest decrease
	worst = ["",1000*1000]
	
	for row in reader:
		#For total number of month
		totalmonths = totalmonths+1
		#For net total amount of profit/losses
		total = total+ int(row[1])
		#For average of the changes in profit/losses
		total1 = total1- int(row[1])
		total2 = total2+ int(row[1])
		#For greatest increase and decrease
		change = int(row[1])-int(prev_row[1])
		if best[1]<change:
			best[1]=change
			best[0]=row[0]
		if worst[1]>change:
			worst[1]=change
			worst[0]=row[0]		
		prev_row=row

output = (
	f"Financial Analysis\n"
	"----------------------------------\n"
	f"Total Months: {totalmonths}\n"
	f"Total: ${total}\n"
	f"Average Change: ${(total1+total2)/(totalmonths-1)}\n"
	f"Greatest Increase in Profits: {best[0]} (${best[1]})\n"
	f"Greatest Decrease in Profits: {worst[0]} (${worst[1]})\n"
	)


print("Financial Analysis")
print("----------------------------------")

#The total number of months included in the data set
#Count the number of lines
#lines= len(list(reader))

print ("Total Months:",totalmonths)

#The net total amount of profit/Losses over the entire period
#sum the profits
print ("Total: $",total)

#The average of the changes in Profit/Losses over the entire period

#mean the profits
print ("Average Change: $",(total1+total2)/(totalmonths-1))


#The greatest increase in profits (date and amount) over the entire period
print (f"Greatest Increase in Profits: {best[0]} (${best[1]})")


#The greatest decrease in losses (date and amount) over the entire period
print (f"Greatest Decrease in Profits: {worst[0]} (${worst[1]})")

# Specify the file to write to
output_path = os.path.join("..", "Output", "bank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
	csvfile.write(output)