#!/usr/bin/env python
import csv
import sys
import decimal
import fileinput
import re
import itertools


def load_transposeddatafile():
  with open('TransposedData.csv') as f:
    transposeddatalist = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],]
    reader = csv.reader(f)
    for row in reader:
        for col in range(2162):
            transposeddatalist[col].append(row[col])
  f.close()    
 
def load_datafile(): 
  with open('Data.csv') as f:
    datalist = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    reader = csv.reader(f)
    for row in reader:
        for col in range(19):
            datalist[col].append(row[col])
            
            pilist = list(set(datalist [13]))
            projlist = list(set(datalist [14]))
            pinumber = len(pilist)
            projnumber = len(projlist)
  f.close()    

def main_option():
    print "Press 1 for information about PIs"
    print "Press 2 for information about project"
    print "Press 3 for information about specific mask/target"
    print "Press 5 to quit:"
    x = raw_input("->")
    return x 


def pi_info():
           print "Press 1 for a list of PIs"
           print "Press 2 for the number of PIs"
           print "Press 5 to quit:"
           pianswer = raw_input("->")
           if pianswer == '1':
                load_datafile()
                load_transposeddatafile()
                print pilist
                listorquit = raw_input('Press 1 for a list of the projects under a certain PI\nPress 5 to quit: ')
                if listorquit == "1":
                    pichoice = raw_input('Enter the name of the PI whose projects you want listed: ')
                    if pichoice in datalist[13]:
                        piprojlist = []
                        for i, j in enumerate(datalist[13]):
                            if j == pichoice:
                                pidatalist = transposeddatalist[i]
                                newlist = pidatalist[14]
                                piprojlist.append(newlist)
                        uniquelist = list(set(piprojlist))
                        print uniquelist
                        numorquit = raw_input('Press 1 for the number of projects under this PI\nPress 5 to quit: ')
                        if numorquit == "1":
                            print len(uniquelist)
                        elif numorquit == "5":
                            sys.exit()
                    else:
                        print('That PI is not part of this database. Please try again')
                if listorquit == "5":
                    sys.exit()
           elif pianswer == '2':
                load_datafile()
                load_transposeddatafile()
                print pinumber
           elif pianswer == "5":
                sys.exit()


def project_info():
           print "Press 1 for a list of projects"
           print "Press 2 for the number of projects"
           print "Press 3 for information about specific target/mask"
           print "Press 5 to quit:"
           projanswer = raw_input("->")
           load_datafile()
           load_transposeddatafile()
           if projanswer == "1":
                load_datafile()
                load_transposeddatafile()
                print projlist
                maskanswer = raw_input('For the masks used in a project, Press 1/nFor the total exposure of a project, Press 2/nFor the number of nights assigned to a project, Press 3/nTo quit, Press 5: ')
                if maskanswer == "1":
                    projname = raw_input('Enter the name of the project of which you want the masks used listed: ')
                    if projname in datalist[14]:
                        masklist = []
                        for i, j in enumerate(datalist[14]):
                            if j == projname:
                                plist = transposeddatalist[i]
                                newlist = plist[2]
                                masklist.append(newlist)
                            uniquelist = list(set(masklist))
                            print uniquelist
                            numorquit = raw_input('For the number of masks used, Press 1. To quit, Press 5: ')
                            if numorquit == "1":
                                print len(uniquelist)
                                sys.exit()
                            elif numorquit == "5":
                                sys.exit()
                            else:
                            	print('That project is not part of this database. Please try again')
                elif maskanswer == "3":
                    projname = raw_input('Enter the name of the project of which you want the to know the number of nights assigned: ')
                    if projname in datalist[14]:
                        masklist = []
                        for i, j in enumerate(datalist[14]):
                            if j == projname:
                                plist = transposeddatalist[i]
                                newlist = plist[7]
                                masklist.append(newlist)
                            uniquelist = list(set(masklist))
                        print len(uniquelist)
                    else:
                        print('That project is not part of this database. Please try again')
                elif maskanswer == "5":
                    sys.exit()
           elif projanswer == "2":
                print projnumber
                load_datafile()
                load_transposeddatafile()
           elif projanswer == "5":
                sys.exit()

def mask_info():
           targetname = raw_input('Enter the name of the specific mask(target name) of which you want to know the total exposure time: ')
           with open('Data.txt') as f: #use data from txt file
              lines = f.readlines()
              totaltimes = []
              for line in lines:
                  if targetname in line:
                     totaltimes.append(line.split()[11]) #append value from elapsedtime/exposuretime collumn (index 11)
           f.close()
           totaltimesfloat = [] #convert items in totaltimes list from strings to floats
           for item in totaltimes:
              totaltimesfloat.append(float(item))
           print sum(totaltimesfloat), "seconds"

     
if __name__== "__main__":
    answer = main_option()  
    while answer != "5":        
        if answer == "1":
           pi_info()
        elif answer == "2": 
           project_info()
        elif answer == "3":
           mask_info()  
        elif answer == "5": 
            sys.exit()
        answer = main_option()
