#!/usr/bin/env python
import csv
import sys

#makes excel cvs data into lists

with open('Data.csv') as f:
    datalist = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    reader = csv.reader(f)
    for row in reader:
        for col in range(19):

#identify lists

            datalist[col].append(row[col])
            pilist = list(set(datalist [13]))
            projlist = list(set(datalist [14]))
            pinumber = len(pilist)
            projnumber = len(projlist)

#making loop

    answer = "7"
    while answer != "5":

#options

        answer = raw_input('Press 1 for list of PIs, Press 2 for number of PIs, Press 3 for list of projects, Press 4 for number of projects, Press 5 to quit:')

#list the PI's

        if answer == "1":   
            print pilist

#number of PI's

        elif answer == "2":
            print pinumber

#list the projects

        elif answer == "3":
            print projlist

#number of projects

        elif answer == "4":
            print projnumber

#exit loop
    
        elif answer == "5":
            sys.exit()
