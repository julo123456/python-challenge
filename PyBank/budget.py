import os
import csv
# list to store data 
date =[]
prof_loss = []
change_prof=[]
previous=0
# read file and statistical calculation
with open("budget_data.csv", mode="r") as csvfile:
    csvbudget = csv.reader(csvfile)
    header = next(csvbudget)
    #for lines  in csvbudget:
       # print(lines)
    for row in csvbudget:
        date.append(row[0])
        prof_loss.append(int(row[1]))
        change_prof.append(int(row[1])-previous)
        previous= int(row[1])

# total number of months in the dataset
    size=len(date)

# net total amount of Profit_Losses 
    total_prof=sum(prof_loss)

# changs in profit_losses and rid of first value in the array
    change_prof.pop(0)

# calculate average change of profit
    average_prof= round(sum(change_prof)/len(change_prof),2)
  
# greatest increase in profits (date and amount) over the entire period
    great_inc= max(change_prof)
  
# greatest decrease in profits (date and amount) over the entire period
    great_dec= min(change_prof)
  
# date where max and min changes are, referenced from index of great_inc and great_dec
max_month=change_prof.index(great_inc)
max_month_=(date[max_month+1])
min_month=change_prof.index(great_dec)
min_month_=(date[min_month+1])

# print ummary statistics
print("Financial Analysis")
print("--------------------------------")
print("Total Months:", str(size))
print("Total:","$"+ str(total_prof))
print("Average Change:", "$"+str(average_prof))
print("Greatest Increase in Profits:", str(max_month_), "$"+ str(great_inc))
print("Greatest Decrease in PRofits:", str(min_month_), "$"+ str(great_dec))

# specify txt file path and write summary statistics into text
output_path=os.path.join("..","output","budget_summary.txt")
f=open("budget_summary.txt","w")
f.write("Financial Analysis\n")
f.write("--------------------\n")
f.write("Total Months:"+ str(size)+'\n')
f.write("Total:" + "$"+ str(total_prof )+ '\n')
f.write("Average Change:" + str(average_prof)+'\n')
f.write("Greatest Increase in Profits:" + " "+ str(max_month_)+ " "+"$"+str(great_inc)+'\n')
f.write("Greatest Decrease in Profits:" + " "+ str(min_month_)+ " "+"$"+str(great_dec)+'\n')
f.close()