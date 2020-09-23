# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:53:57 2020

@author: Dylan Pandjaris
"""

import csv
import xlsxwriter

class DataStructure():
    def __init__(self, name, avail):
        self.name = name
        self.avail = avail
        
with open ("data2.csv") as csvfile:
    data = []
    readcsv = csv.reader(csvfile, delimiter = ",")
    cnt = 1
    for row in readcsv:
        name = row[0]
        avail = []
        if cnt >= 6:
            if name == 'Liam **McConnell**':
                name = 'Liam McConnell'
            if name == "Liam":
                continue
            for col in row:
                if col == "OK":
                    avail.append(1)
                elif col == "":
                    avail.append(0)
        cnt += 1
        data.append(DataStructure(name, avail))
        
    data = data[6:]
    data = data[:-1]
    data.append(DataStructure("Cale Hupe", [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
    # data.append(DataStructure("Morgan Meadows", [0, 1, 0, 0, 0, 1, 0, 0, 0, 1]))

# for i in range(len(data)):
#     print(data[i].name, data[i].avail)
    
# print("")
# print("")
# print("")

waste = [2, 3, 6, 7, 10]
for person in data:
    newAvail = []
    for i in range(len(person.avail)):
        if i not in waste:
            newAvail.append(person.avail[i])
    person.avail = newAvail

losers = 0
total = 0
for person in data:
    print(person.name, person.avail)
    if sum(person.avail) == 0:
        losers += 1
    total += 1

print("")

print(total, "people in total")
print(losers, "people completely unavailable")
print(total - losers, "people available")

# Prune the data
temp = []
for person in data:
    if sum(person.avail) > 0:
        temp.append(person)
data = temp

names = []
avails = []
for person in data:
    names.append(person.name)
    avails.append(person.avail)

print("")
print("")
    
print(names)
print(len(names))
print("")

print(avails)
print(len(avails))
print("")
# print(len(data))


# Load solution as csv here

workbook = xlsxwriter.Workbook('Output.xlsx')
worksheet = workbook.add_worksheet("Main")

worksheet.write(0, 0, "Week")

days = ["Monday", "Wednesday", "Friday"]
for i in range(len(days)):
    worksheet.write(0, i+1, days[i])
    
for i in range(3):
    worksheet.write(i+1, 0, i+1)

workbook.close()


