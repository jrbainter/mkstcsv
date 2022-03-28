#!/usr/bin/env python3

import pdb
import sys
from enum import IntEnum

#Input field numbers in .csv file
class Fds(IntEnum):
	descrip = 10
	dtopen = 11
	dtclose = 4
	proceeds = 14
	price = 17

# Input field positions
#FDP = [10,11,4,14,17]

# Header for output file.
HDR = "Owner,Description,DtAcquired,DtSold,SalesPrice,Cost\n"
# Owner of Transaction 'T'|'S'|'J'
OWNER = 'J'

# Substitude text for a value of zero
TSUB = "0"


def get_filenames():
	# Get File Names
	mes1 = "Enter Input File Name: "
	mes2 = "Enter Output File Name: "
	mes3 = "Are File Names Correct? y/n: "
	while True :
		ifn = input(mes1)
		ofn = input(mes2)
		print()
		print("File Names: {:s} {:s}".format(ifn,ofn))
		ans = input(mes3)
		if ans in ['Y','y']: break
	return (ifn,ofn)

def shortdec(ldes):
	""" This function shortens the intext"""
	ld = ldes.split()
	st = ld[0]+" "+ld[len(ld)-1]
	return st

def mktscsv(ifn,ofn):
	""" This program is used to make a Tax Slayer .csv file
	from a TDAmeritrade .csv file. The TDAmeritrade .xlsx file
	is used to create the TDAneritrade .csv file by opening the
	.xlsx filewith a spreadsheet ap[plication and then saving
	the file as a .csv file.
	"""

# Open files
	try:
		with open(ifn,'r') as infile, open(ofn, 'w') as outfile:
			dh = infile.readline() # skip input file header line
			outfile.write(HDR) # write out file header
			for line in infile:
				sl = line.split(',')
				ol = []
				ol.append(OWNER)
				for fd in Fds:
					data = sl[fd.value]
					if fd.name == "descrip": data = shortdec(data)
					if  (fd.name == "proceeds" or fd.name == "price")\
						and data == "0": data = TSUB
					ol.append(data)
				outline = ",".join(ol)+'\n'
				outfile.write(outline)

	except Exception as e:
		print("Error Opening ", str(e))





if __name__ == "__main__":

	#  inf, outp = "TestIn.csv", "TestOut.csv"
	if len(sys.argv) == 3:
		mktscsv(sys.argv[1], sys.argv[2])
	else:
		mktscsv(get_filenames())

