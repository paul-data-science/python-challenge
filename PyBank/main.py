# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:34:43 2018

@author: Paul Ag (github name: paulXLV)
"""

import csv

inputfile='\\Users\\Paul-DS\\Downloads\\budget_data.csv'
outputfile='\\Users\\Paul-DS\\Downloads\\budget_output.txt'

profit_loss=[]
pl_summary={}

with open(inputfile, newline='') as csvfile:
    # read and split the data on commas and put into string variable budget_reader
    budget_reader=csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(budget_reader)
    
    total=0
    total_months=0
    # Convert budget_reader string to a list profit_loss
    for line in budget_reader:
        profit_loss.append(line)
        # The total net amount of "Profit/Losses" over the entire period
        total+=int(line[1])
        # The total number of months included in the dataset
        total_months+=1
       
    subtract_MoM=0
    tot_MoM=0
    Avg_Mom=0
    # Initialize max increase and max decrease values with latest increase/decrease value
    max_decrease=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    max_increase=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    # Compute the change in "Profit/Losses" between months over the entire period
    # by iterating (backwards) from latest month-year to the earliest
    for i in range(total_months,1,-1): # stops when i is 2
        subtract_MoM=int(profit_loss[i-1][1])-int(profit_loss[i-2][1])
        # Find the Greatest Increase (max_increase) and Greatest Decrease (max_decrease)
        if subtract_MoM < max_decrease:
            min_month_yr=profit_loss[i-1][0]
            max_decrease=subtract_MoM
        elif subtract_MoM > max_increase:
            max_increase=subtract_MoM
            max_month_yr=profit_loss[i-1][0]
        # Total amount change in "Profit/Losses" between months over the entire period
        tot_MoM=tot_MoM+subtract_MoM
    #The average change in "Profit/Losses" between months over the entire period    
    Avg_MoM=tot_MoM/(total_months-1)
        

'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''
text_file=open(outputfile,"w")
text_file.write('Financial Analysis')
print('Financial Analysis')
text_file.write('\n----------------------------')
print('----------------------------')
text_file.write('\nTotal Months: '+str(total_months))
print('Total Months: '+str(total_months))
text_file.write('\nTotal: $'+str(total))
print('Total: $'+str(total))
text_file.write('\nAverage  Change: $'+str(round(Avg_MoM,2)))
print('Average  Change: $'+str(round(Avg_MoM,2)))
text_file.write('\nGreatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
text_file.write('\nGreatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')

text_file.close()

