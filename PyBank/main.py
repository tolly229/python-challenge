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

    averageChange = sum(profit) / int(len(month))  

    print("Financial Analysis")
    print("----------------------------------------------------")
    print(f"Total Months: {len(month)}")
    print(f"Total: $ {sum(profit)}")
    print(f"Average Change: $ {(averageChange)}")
    print(profit_losses)

    
    
    
    
    #print(f"Greatest Increase in Profits:  {str(greatIncreaseMonth) + {str(greatIncreaseAmount)})
    #print( \n"Greatest Decrease in Profits: " + {str(greatDecreaseMonth)} + {str(greatDecreaseAmount)})


    

