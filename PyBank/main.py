import csv
import os

#import and open given csv file
csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as file:
#create a csv reader object to read the data    
    reader = csv.reader(file)
    header = next(reader)

#initialize variable and create lists to store data
    total_months = 0
    total_revenue = 0
    revenue_change = 0
    prev_revenue = 0
    revenue_change_list = []
    revenue_change_avg = 0
    max_revenue_change = 0
    min_revenue_change = 0
    max_revenue_change_date = ""
    min_revenue_change_date = ""

#loop through each row of data to calculate total months, total revenue, and revenue change
    for row in reader:
        total_months += 1 #for total months
        total_revenue += int(row[1]) #for total revenue

#for revenue change and revenue change list if its not
#the first row of data calculate change and append to list
#else set previous revenue to the first row of data
        if prev_revenue != 0:
            revenue_change = int(row[1]) - prev_revenue
            prev_revenue = int(row[1])
            revenue_change_list.append(revenue_change)
        else:
            prev_revenue = int(row[1])

#calculate greatest increase and decrease in profits
        if revenue_change > max_revenue_change:
            max_revenue_change = revenue_change
            max_revenue_change_date = row[0]
        if revenue_change < min_revenue_change:
            min_revenue_change = revenue_change
            min_revenue_change_date = row[0]

#calculate average revenue change  
    revenue_change_avg = round(sum(revenue_change_list) / len(revenue_change_list),2)
 
#print results to terminal 
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_revenue}")
    print(f"Average Change: ${revenue_change_avg}")
    print(f"Greatest Increase in Profits: {max_revenue_change_date} (${max_revenue_change})")
    print(f"Greatest Decrease in Profits: {min_revenue_change_date} (${min_revenue_change})")

#create text file to write results to
    pathoutput = os.path.join("analysis","budget_data_output.txt")  
    with open(pathoutput, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${total_revenue}\n")
        file.write(f"Average Change: ${revenue_change_avg}\n")
        file.write(f"Greatest Increase in Profits: {max_revenue_change_date} (${max_revenue_change})\n")
        file.write(f"Greatest Decrease in Profits: {min_revenue_change_date} (${min_revenue_change})\n")
        file.close()

