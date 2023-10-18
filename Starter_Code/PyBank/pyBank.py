import os
import csv
file = "/Users/mattgarcia/Desktop/python_homework/Python_attempt/Starter_Code/PyBank/Resources/budget_data.csv"
total_months = 0
net_total = 0
total_change = 0
change_count = 0
with open(file) as bank_file:
    #print("Opened the file")
    csvReader = csv.reader(bank_file)
   #print(csvReader)
    bank_file_header = next(csvReader)
    #print(bank_file_header)
    prev_profit_loss = None
    for row in csvReader:
        #Checking if the row has values first
        if row and row[0]:
            total_months += 1
        if row and row[1]:
            net_total += int(row[1])
        if row:
            profit_loss = int(row[1])
            if prev_profit_loss is not None:
                change = profit_loss - prev_profit_loss
                total_change += change
                change_count += 1
            prev_profit_loss = profit_loss
    
    average_change = total_change / change_count
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: {average_change}")