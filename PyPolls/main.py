# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:24:18 2018

@author: Paul Aggarwal (github name: paulXLV)
"""
import csv

# Create empty list
polls=[]
# Create empty dictionary
dict_polls={}
# Create empty dictionaty
dict_summary={}
# Open file and assign to csvfile object name
with open('\\Users\\Paul-DS\\Downloads\\election_data.csv', newline='') as csvfile:
    # read and split the data on commas
    pollreader=csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(pollreader)
    # Convert list object to a list 
    for line in pollreader:
        polls.append(line)
    # Convert List into Dictionary for Grouping Names
    for line in polls:
        name_key=line[2]
        if name_key not in dict_polls:
           # insert name_key into dictionary and initialize to 0
            dict_polls[name_key]=0
        # count the name key inside dictionary
        dict_polls[name_key]+=1
    
    # Compute the percentages of each name key of dict_polls and insert into dict_summary
    total_polls=len(polls)
    for name in dict_polls:
        dict_summary[name]=int((dict_polls[name]/total_polls)*100)
        
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
    # winner=[]
    # Initialize the highest value to comapre
    highest=0
    for name in dict_summary:
        if highest < dict_summary[name]:
            highest=dict_summary[name]
            winner=name
    
        
    
print(len(polls))
# print(candidate)
print(dict_polls)
print(dict_summary)
print(winner)
# sum of all grouped names match total number as checked on calc
#print(max(zip(dict_summary.values(),dict_summary.keys())))