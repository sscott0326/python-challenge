#Dependencies
import os
import csv



#Set path for file
pypoll_csv_path = os.path.join('Resources', 'election_data.csv')

#Open the csv
with open(pypoll_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",", skipinitialspace=True)

    #Defining variables

    #Total votes holds the total number of votes cast
    #Candidate contains a list of all the unique Candidates in the poll
    total_votes = 0
    Candidate = []

    #The following variables hold the # of votes and % of total_votes for each candidate
    Khan_votes = 0
    Khan_percent = 0.0
    Correy_votes = 0
    Correy_percent = 0.0
    Li_votes = 0
    Li_percent = 0.0
    Otooley_votes = 0
    Otooley_percent = 0.0

    #Store the header
    header = next(csvreader)

    #For loop that counts through the rows
    for row in csvreader:

        #Add 1 to total_votes for each row
        total_votes += 1

        #If the candidate is not in the candidate list, add the candidate's names to the list
        if row[2] not in Candidate:
            Candidate.append(row[2])

        #If the candidate is in the candidate, add votes to the corresponding candidate that each vote is for
        if row[2] in Candidate:
            if row[2] == "Khan":
                Khan_votes += 1
            if row[2] == "Correy":
                Correy_votes += 1
            if row[2] == "Li":
                Li_votes += 1
            if row[2] == "O'Tooley":
                Otooley_votes += 1

#Calculating the percent of total votes that each candidate received, to the nearest 3 decimal places
Khan_percent = round((Khan_votes/total_votes)*100, 3)
Correy_percent = round((Correy_votes/total_votes)*100, 3)
Li_percent = round((Li_votes/total_votes)*100, 3)
Otooley_percent = round((Otooley_votes/total_votes)*100, 3)

#Creates a dictionary containing the different candidates and the total votes that each one received
candidate_votes = {'Khan': Khan_votes, 'Correy': Correy_votes, 'Li': Li_votes, "O'Tooley": Otooley_votes}
#The winner has the most votes
winner = max(candidate_votes, key=candidate_votes.get)

#Print final results       
final_results = f"""
Election Results
{'-'*25}
Total Votes: {total_votes}
{'-'*25}
Khan: {Khan_percent}% ({Khan_votes})
Correy: {Correy_percent}% ({Correy_votes})
Li: {Li_percent}% ({Li_votes})
O'Tooley: {Otooley_percent}% ({Otooley_votes})
{'-'*25}
Winner: {winner}
{'-'*25}
"""
print(final_results)

#Output final results in to a text file
f = open('election_results.txt','w')
f.write(final_results)
f.close()