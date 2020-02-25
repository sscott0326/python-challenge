#Dependencies
import os
import csv
from statistics import mean

#Defining variables

#Total_months counts the number of months in the data
#Net_total adds all of the numbers in the Profit/Losses together
total_months = 0
net_total = 0

#Previous_month stores the profit/loss amount for the month prior
#Profit/loss differences are calculated with monthly_difference then stored in the list monthly_change
previous_month = 0
monthly_difference = 0
monthly_change = []
average_change = 0

#Store month name and value for the greatest increase and decrease in Profit/Loss
greatest_increase = 0
greatest_month = 'greatest'
greatest_decrease = 0
least_month = 'least'


#Set path for file
pybank_csv_path = os.path.join('Resources', 'budget_data.csv')

#Open the csv
with open(pybank_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    #Store the header line
    csv_header = next(csvreader)

    #Stores the first row of data
    #Set up the previous_month variable, necessary for calculating differences in profit
    #total_months and net total add their values
    first_month = next(csvreader)
    previous_month = int(first_month[1])
    net_total += previous_month
    total_months +=1

    
    #For loop to count through rows
    for row in csvreader:   
        
        #For each row, add 1 to total months and add the profit/loss amount to net_total
        total_months += 1
        net_total += int(row[1])

        #Calculating monthly_difference then adding it to the monthly_change list
        monthly_difference = (int(row[1]) - previous_month)
        monthly_change.append(monthly_difference)

        #Checking if each monthly difference is the largest or the least, 
        #then storing the information about that month if true
        if monthly_difference == max(monthly_change):
            greatest_increase = monthly_difference
            greatest_month = row[0]
        if monthly_difference == min(monthly_change):
            greatest_decrease = monthly_difference
            least_month = row[0]

        #Setting the current profit/loss amount to the previous_month variable before moving on to the next row
        previous_month = int(row[1])


#Calculating the average change
average_change = mean(monthly_change)
    
#Printing out final summary
final_summary = f"""
Financial Analysis
{'-'*25}
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_month} (${greatest_increase})
Greatest Decrease in Profits: {least_month} (${greatest_decrease})
{'-'*25}
"""
print(final_summary)

#Output a text file with the results
f = open('financial_analysis.txt','w')
f.write(final_summary)
f.close()
