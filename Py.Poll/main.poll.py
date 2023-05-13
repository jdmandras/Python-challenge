#Import module
#Create filepath across operating systems
import os
import csv

csvpath = os.path.join('RESOURCES/election_data.csv')

#List for candidates name
candidate = []

#List for number of votes per candidate
cand_votes = []

#List for percent of votes per candidate
per_votes = []

#Counter for number of votes
votes_total = 0

#Open and read the CSV file (note: ALL COMMANDS UNDER THIS!)
with open(csvpath) as csvfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Reading header
    csv_header = next(csvreader)

    #For loop candidates name and vote count
    for row in csvreader:
        #Add to vote counter
        votes_total = votes_total + 1

        #Record candidate name (if not already in the list) and add a vote to their name
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            cand_votes.append(1)
        else:
            index = candidate.index(row[2])
            cand_votes[index] = cand_votes[index] + 1

    #For loop candidates percent votes
    for votes in cand_votes:
        percent = (votes/votes_total) * 100
        percentage = "%.3f%%" % percent
        per_votes.append(percentage)

    #Name winning candidate
    winner = max(cand_votes)
    index = cand_votes.index(winner)
    win_c = candidate[index]

#Print to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(votes_total)}")
print("--------------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {str(per_votes[i])} ({str(cand_votes[i])})")
print("--------------------------")
print(f"Winner: {win_c}")
print("--------------------------")

#Export to txt file
output = open("ANALYSIS.P/results.txt","w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(votes_total)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate)):
    line = str(f"{candidate[i]}: {str(per_votes[i])} ({str(cand_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {win_c}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

