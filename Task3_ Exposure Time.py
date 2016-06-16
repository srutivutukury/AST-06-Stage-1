#!/usr/bin/python

import sys, argparse, csv

# command arguments
parser = argparse.ArgumentParser(description='csv to postgres',\
 fromfile_prefix_chars="@" )
parser.add_argument('file', help='csv file to import', action='store')
args = parser.parse_args()
TransposedData.csv = args.file

# open csv file
with open("Transposed Data.csv", 'rb') as csvfile:

#after parsing through a csv file and extract the data from only collumn 10(exposure time) of a specific targetname.
#Total exposure time on each mask (adding the times in column "exposure time") under a single project/targetname/object

	def exposuretime(targetname):
		totaltimes = []
		reader = csv.reader('Transposed Data.csv', delimiter=' ')
        	elapsed_time = [10]
    	for row in reader:
    		match = re.search(r'targetname', line)
			if match:
				totaltimes.append(row[10])
		print sum(totaltimes), "seconds"
	
	if __name__== "__main__":
		
		exposuretime(03323261-273754)
