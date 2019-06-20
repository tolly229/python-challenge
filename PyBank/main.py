import os
import csv
currentdir = os.getcwd()
path = os.path.join("budget_data.csv")
with open(path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    headers = next(csvreader)
    first_row = next(csvreader)

    month = []
    profit = []
    profit_losses = []
    previous_value = first_row[1]

    for row in csvreader: 
        
        month.append(row[0])
        profit.append(int(row[1]))
        
        profit_losses.append(int(row[1])-int(previous_value))

        previous_value = row[1]

    averageChange = sum(profit_losses) / int(len(month))  

    print("Financial Analysis")
    print("----------------------------------------------------")
    print(f"Total Months: {len(month)+1}")
    print(f"Total: $ {sum(profit)+ int(first_row[1])}")
    print(f"Average Change: $ {(averageChange)}")
    print(f"Greatest Increase in Profits: {max(profit_losses)}")
    print(f"Greatest Decrease in Profits: {min(profit_losses)}")

    #print(row[max(profit)])

with open('mainFinal.txt', 'w') as txtfile:
    final_results = (
    f"\nFinancial Analysis\n"    
    f"----------------------------------------------------\n"
    f"Total Months: {len(month)+1}\n"
    f"Total: $ {sum(profit)+ int(first_row[1])}\n"
    f"Average Change: $ {(averageChange)}\n"
    f"Greatest Increase in Profits: {max(profit_losses)\n}"
    f"Greatest Decrease in Profits: {min(profit_losses)}\n)
    txtfile.write(final_results)

