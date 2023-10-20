import os
import csv
#Initialzing variables 
file = "/Users/mattgarcia/Desktop/python_homework/Python_attempt/Starter_Code/PyPoll/Resources/election_data.csv"
output_file = "pyPoll_Analysis.txt"
total_votes = 0
candidates = []
candidate_votes = {}
winner = ""
popular_vote = 0
with open(file) as poll_file:
    csvreader = csv.reader(poll_file)
    poll_file_header = next(csvreader)
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        #Checks if candidate is already in the dictonary, if so add 1 to their
        #votes, if not create a new key value with the candidate as the key and their total votes as 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    candidates = list(candidate_votes.keys())
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    #Time to find the votes percentage and who won
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100
        print(f"{candidate}: {vote_percentage:.2f}% ({votes})")

        if votes > popular_vote:
            winner = candidate
            popular_vote = votes
    print("------------------------------")
    print(f"Winner: {winner}")

#Now to write the output to a separate file
with open(output_file, 'w') as out:
    out.write("Election Results\n")
    out.write("---------------------------\n")
    out.write(f"Total Votes: {total_votes}\n")
    out.write("---------------------------\n")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100
        out.write(f"{candidate}: {vote_percentage:.2f}% ({votes})\n")
    out.write("----------------------------\n")
    out.write(f"Winner: {winner}\n")
        
