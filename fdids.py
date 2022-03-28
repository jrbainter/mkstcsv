#!/usr/bin/env python3

import sys

def get_filename():
	while True:
		fn = input("Enter name of input file: ")
		print(); print(f"File name is: {fn}")
		ans = input("File name correct(yn)? ")
		if ans in "Yy": break
	return fn

def fdids(fn):
	""" fdids prints the field names and number
	of the Header line in a .csv file to stdout.
	Invoke with the fdids command with the header
	file name as the first argument to the command as follows:

		python3 fdids.py xxx.csv or
		./fdids.py xxx.csv

	If file name is not provided on the command line the
	script will promp the user for the filename.
	"""

	infile = open(fn)
	line = (infile.readline()).strip()
	infile.close()
	llist = line.split(',')
	for count,ele in enumerate(llist,1):
		fl = "{:18s} {:4d}  ".format(ele,count-1)
		print(fl, end="")
		if count%4 == 0: print()
	print()

if __name__ == "__main__":
	if len(sys.argv) == 2: fn = sys.argv[1]
	else: fn = get_filename()
	fdids(fn)
