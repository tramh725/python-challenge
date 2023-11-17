import csv
import os 
budget_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

months = []
earn = []
monthly_profits = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    csv_header= next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        months.append(row[0])
        earn.append(int(row[1]))
        
    for i in range(len(earn)-1):
        monthly_profits.append(earn[i+1]-earn[i])

increase_value = max(monthly_profits)
increase_month = monthly_profits.index(max(monthly_profits)) + 1

decrease_value = min(monthly_profits)
decrease_month = monthly_profits.index(min(monthly_profits)) + 1
      
print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(earn)}")
print(f"Average Change: ${round(sum(monthly_profits)/len(monthly_profits),2)}")
print(f"Greatest Increase in Profits: {months[increase_month]} (${increase_value})")
print(f"Greatest Decrease in Profits: {months[decrease_month]} (${decrease_value})")

text_file = os.path.join("PyBank", "analysis")
with open(text_file, "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("--------------------------------------", file=text_file)
    print(f"Total Months: {len(months)}", file=text_file)
    print(f"Total: ${sum(earn)}", file=text_file)
    print(f"Average Change: ${round(sum(monthly_profits)/len(monthly_profits),2)}", file=text_file)
    print(f"Greatest Increase in Profits: {months[increase_month]} (${increase_value})", file=text_file)
    print(f"Greatest Decrease in Profits: {months[decrease_month]} (${decrease_value})", file=text_file)