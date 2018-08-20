# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:34:43 2018

@author: Paul Ag (github name: paulXLV)
"""

import csv

profit_loss=[]
pl_summary={}
with open('\\Users\\Paul-DS\\Downloads\\budget_data.csv', newline='') as csvfile:
    # read and split the data on commas
    budget_reader=csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(budget_reader)
    # Convert list object to a readable/printable list 
   
    total=0
    total_months=0
    for line in budget_reader:
        profit_loss.append(line)
        total+=int(line[1])
        total_months+=1
        
    # Convert List into Dictionary for Grouping Names
    '''for line in polls:
        name_key=line[2]
        if name_key not in dict_polls:
           # insert name_key into dictionary and initialize to 0
            dict_polls[name_key]=0
        # count the name key inside dictionary
        dict_polls[name_key]+=1
        '''
print(profit_loss)