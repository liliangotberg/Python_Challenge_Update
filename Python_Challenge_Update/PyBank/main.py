# import os library to generate a path to our csv file
# import csv library to read our csv file
import os
import csv

# create new variable "csv_path" and assign it to path module "os.path.join" to read csv file in Resource folder
csv_path = os.path.join('Resources', 'budget_data.csv')

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# begin by opening csv file in a iterabable format, like a dictionary where objects can be looped
# use Python 'with' command and 'open()' function; ("filename" (csv_path),"mode" (newline= " ")) 
# the argument "newline="" is set to empty quotes in order for loop to reiterate from one row to the next 
# keep block of code within its scope of with command; make sure to indent subsequent code
with open(csv_path, newline="") as financial_data:
    reader = csv.reader(financial_data)
    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)
 
# to process analysis, create "output" variable to equal an object
# object is formatted with f'strings to create a legible result
# reset block scope
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# preview output
print(output)

# create text file to export results, create file path to folder
analysis_outcome = os.path.join('Resources', 'budget_analysis.txt') 
 # write to file but need an argument to enter in next file, set as its own variable (output - f'string format)
with open(analysis_outcome, 'w') as txt_file:
    txt_file.write(output) #write is now a method, pass an object/ argument 