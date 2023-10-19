import os
import csv
file = "/Users/mattgarcia/Desktop/python_homework/Python_attempt/Starter_Code/PyPoll/Resources/election_data.csv"
total_votes = 0
candidates = []
prev_candidate = None
with open(file) as poll_file:
    #print("Opened the file")
    csvreader = csv.reader(poll_file)
    poll_file_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row and row[2] != prev_candidate:
            prev_candidate = row[2]
            candidates.append(prev_candidate)
    #print(candidates)