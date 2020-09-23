# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:01:51 2020

@author: Dylan Pandjaris
"""

import csv


class Data_structure(object):
    def __init__(self, names, day, time):
        self.names = names
        self.day = day
        self.time = time


def day_calc(cnt):
    if cnt < 34:
        return("Monday")
    if cnt < 38:
        return("Tuesday")
    if cnt < 42:
        return("Wednesday")
    if cnt < 46:
        return("Thursday")
    else:
        return("Friday")
        
def time_calc(cnt):
    if (cnt - 31) % 4 == 0:
        return("9:30")
    if (cnt - 31) % 4 == 1:
        return("10:30")
    if (cnt - 31) % 4 == 2:
        return("1:30")
    else: #if (cnt - 31) % 4 == 3:
        return("2:30")
    

data = []
with open ("availability.csv") as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
    cnt = 1
    for row in readcsv:
        if cnt >= 31:
            day = day_calc(cnt)
            time = time_calc(cnt)
            names = []
            for i in range(2, 27):
                if row[i] != 0:
                    names.append(row[i].upper())
            data.append(Data_structure(names, day, time))
        cnt += 1

all_names = []
for i in range(len(data)):
    for j in range(len(data[i].names)):
        if data[i].names[j] not in all_names:
            all_names.append(data[i].names[j])
        #print(data[i].names[j])
#all_names.pop(-14)
        
availability = []
for i in range(len(data)):
    row = []
    for k in range(len(all_names)):
        cnt = 0
        for j in range(len(data[i].names)):
            if all_names[k] == data[i].names[j]:
                cnt += 1
                break
        row.append(cnt)
    availability.append(row)

#for i in range(len(availability)):
#    availability[i].pop(-14)

def hole_finder(beginning, end):
    for i in range(len(availability)):
        cnt = 0
        for j in range(len(availability[i][beginning:end])):
            if availability[i][j] == 1:
                cnt += 1
        print(cnt)

#hole_finder(0:22)
        
def availability_chunk(beginning, end):
    new_array = []
    for i in range(len(availability)):
        row = []
        for j in range(beginning, end + 1):
            row.append(availability[i][j])
        new_array.append(row)
    return(new_array)
    
def name_chunk(beginning, end):
    new_array = []
    for i in range(beginning, end + 1):
        new_array[i].append(all_names[i])
    new_array = str(new_array).replace("'", '"')
    return(new_array)

def availability_pattern(frequency, group):
    new_array = []
    for i in range(len(availability)):
        row = []
        for j in range(group - 1, len(availability[i]), frequency):
            row.append(availability[i][j])
        new_array.append(row)
    return(new_array)
    
def name_pattern(frequency, group):
    new_array = []
    for i in range(group - 1, len(all_names), frequency):
        new_array.append(all_names[i])
    new_array = str(new_array).replace("'", '"')
    return(new_array)

print(availability_pattern(3, 3))
#print(' ')
print(name_pattern(3, 3))
##print(' ')
#print(name_pattern(3, 1))
#print(len(name_pattern(3, 1)))
    
#for i in range(len(availability_pattern(3, 2))):
    #print(len(availability_pattern(3, 1)[i]))




           