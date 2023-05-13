#Import module
#Create filepath across operating systems
import os
import csv

csvpath = os.path.join('RESOURCES/budget_data.csv')

#Variables (in order: months, profit/loss, starting amount, change, dates, profits)
months = 0
total = 0
start = 0
change = 0
dates = []
profits = []

#Open and read the CSV file (note: ALL COMMANDS UNDER THIS!)
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Reading header
    csv_header = next(csvreader)
    #Reading first row for starting points - ignore dates
    first_row = next(csvreader)
    months = months + 1
    total = int(first_row[1])
    start = int(first_row[1])
    
    #For loop (excluding header & first row)
    for row in csvreader:
        #Tracking dates
        dates.append(row[0])

        #Calculate changes 
        change = int(row[1])-start
        profits.append(change)
        start = int(row[1])

        #Note number of months
        months = months + 1 

        #Total net profits/loss over whole data
        total = total + int(row[1])

#Calculate average change
avg_change = sum(profits)/len(profits)

#Calculate Greatest Increase in profits
great_inc = max(profits)
inc_index = profits.index(great_inc)
inc_date = dates[inc_index]

#Calculate Greatest Decrease in profits
great_dec = min(profits)
dec_index = profits.index(great_dec)
dec_date = dates[dec_index]

#Print in terminal
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total))
print("Average Change: $" + str(round(avg_change,2)))
print(f"Greatest Increase in Profits: {inc_date} (${str(great_inc)})")
print(f"Greatest Decrease in Profits: {dec_date} (${str(great_dec)})")


#Export to txt file
output = open("ANALYSIS.B/results.txt","w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(months)}")
line4 = str(f"Total: ${str(total)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {inc_date} (${str(great_inc)})")
line7 = str(f"Greatest Decrease in Profits: {dec_date} (${str(great_dec)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))


