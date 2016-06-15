#!/usr/bin/env python
import csv
import sys
#makes data into lists

with open('C:\Users\Ogni\Documents\GitHub\AST-06-Stage-1\Data.csv') as f:
    datalist = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    reader = csv.reader(f)
    for row in reader:
        for col in range(19):
            datalist[col].append(row[col])
            pilist = list(set(datalist [13]))
            projlist = list(set(datalist [14]))
            pinumber = len(pilist)
            projnumber = len(projlist)     
    answer = "7"
    while answer != "5":
        answer = raw_input('Press 1 for list of PIs, Press 2 for number of PIs, Press 3 for list of projects, Press 4 for number of projects, Press 5 to quit:')
        if answer == "1":   
            print pilist
        elif answer == "2":
            print pinumber
        elif answer == "3":
            print projlist
        elif answer == "4":
            print projnumber
        elif answer == "5":
            sys.exit()
