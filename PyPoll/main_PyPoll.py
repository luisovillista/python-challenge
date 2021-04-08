import os
import csv

with open('PyPoll/Resources/election_data.csv','rt')as f:
 data = csv.reader(f)
  
Py_Poll_csv = ('PyPoll/Resources/election_data.csv')

count = 0
candidate_list = []
candidate = []
vote_count = []
vote_percent = []

with open(Py_Poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        count = count + 1
        
        candidate_list.append(row[2])
    
    sorted_list = sorted(vote_count)
    arrange_list = sorted_list
    

    for x in set(candidate_list):
        candidate.append(x)
        
        y = candidate_list.count(x)
        vote_count.append(y)
        
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = candidate[vote_count.index(winning_vote_count)]

    print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes: " + str(count))    
print("-------------------------")
for i in range(len(candidate)):
            print(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

with open('PyPoll_election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate))):
        text.write(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")