# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:34:43 2018

@author: Paul Ag (github name: paulXLV)
"""

import csv

total1=[] # check to see if total sum is correct
profit_loss=[]
pl_summary={}
with open('\\Users\\Paul-DS\\Downloads\\budget_data.csv', newline='') as csvfile:
    # read and split the data on commas and put into string variable budget_reader
    budget_reader=csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(budget_reader)
    # Convert budget_reader string to a list profit_loss
    # Count total months
    # Total sum in dollars
    total=0
    total_months=0
    for line in budget_reader:
        profit_loss.append(line)
        total1.append(int(line[1]))
        total+=int(line[1])
        total_months+=1
        
    # find Largest increase/decrease and save month-year and revenue together in list
    # First initialize lowest and highest lists with next value on list
    min_value=profit_loss[1][1]
    max_value=profit_loss[1][1]
    for value in profit_loss:
        # print(value)
        if int(value[1]) < int(min_value):
            min_month_yr=value[0]
            min_value=value[1]
           # print(min_value)
        elif int(value[1]) > int(max_value):
            max_value=value[1]
            max_month_yr=value[0]
           # print(max_value)
    

# print(profit_loss)
print('month count: ', total_months)
print('total: ',total)
print('highest: ',max_month_yr,', ',max_value)
print('lowest: ',min_month_yr,', ',min_value)

#print(avg(total1))