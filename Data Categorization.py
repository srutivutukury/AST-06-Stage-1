#!/usr/bin/env python
import csv

#makes data into lists

with open('C:\Users\Ogni\Documents\GitHub\AST-06-Stage-1\Data.csv') as f:
    datalist = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    reader = csv.reader(f)
    for row in reader:
        for col in range(19):
            datalist[col].append(row[col])
        #print datalist
print('Press 1 for list of PIs, Press 2 for number of PIs, Press 3 for list of projects, Press 4 for number of projects:')

#list of PI's
if raw_input == '1':   
    pilist = list(set(datalist [13]))
    print pilist
    
#number of unique PI's
    pinumber = len(pilist)
    #print pinumber

#list of projects
    projlist = list(set(datalist [14]))
    #print projlist

#number of projects
    projnumber = len(projlist)
    #print projnumber


