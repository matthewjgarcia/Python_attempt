import os
import csv
file = "/Users/mattgarcia/Desktop/python_homework/Python_attempt/Starter_Code/PyPoll/Resources/election_data.csv"
total_votes = 0
candidates = []
candidate_votes = {}
prev_candidate = None
with open(file) as poll_file:
    #print("Opened the file")
    csvreader = csv.reader(poll_file)
    poll_file_header = next(csvreader)
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        #Checks if candidate is already in the dictonary, if so add 1 to their
        #votes, if not create a new key value with the candidate as the key and their
        #total votes as 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    candidates = list(candidate_votes.keys())
    #print(candidates)
    #print(candidate_votes)
        
