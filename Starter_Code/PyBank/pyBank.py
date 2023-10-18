import os
import csv
file = "/Users/mattgarcia/Desktop/python_homework/Python_attempt/Starter_Code/PyBank/Resources/budget_data.csv"
total_months = 0
net_total = 0
total_change = 0
change_count = 0
greatest_increase_date = None
greatest_increase_amt = 0
greatest_decrease_date = None
greatest_decrease_amt = 0
prev_profit_loss = None
with open(file) as bank_file:
    #print("Opened the file")
    csvReader = csv.reader(bank_file)
   #print(csvReader)
    bank_file_header = next(csvReader)
    #print(bank_file_header)
    for row in csvReader:
        date = row[0]
        profit_loss = int(row[1])
        #Checking if the row has values first
        if row and row[0]:
            total_months += 1
        if row and row[1]:
            net_total += profit_loss
        if row:
            profit_loss = int(row[1])
            if prev_profit_loss is not None:
                change = profit_loss - prev_profit_loss
                total_change += change
                change_count += 1
                if change > greatest_increase_amt:
                    greatest_increase_date = date
                    greatest_increase_amt = change
                if change < greatest_decrease_amt:
                    greatest_decrease_date = date
                    greatest_decrease_amt = change
            prev_profit_loss = profit_loss
    
    average_change = total_change / change_count
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amt})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amt})")

    #Trying to get the greatest increase working, stuck on lines 32 ish