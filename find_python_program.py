#!/usr/bin/python3
import os
import glob
import argparse
import sys

parser = argparse.ArgumentParser(description="Finds python programs with the name given. Only works on Linux and if python_programs directory already exists.")
parser.add_argument("-f", "--file", help='python find_python_program.py [-f|--file] <filename>')
parser.add_argument('-s', '--search', help='python find_python_program.py -f <filename> [-s|--search] <relatedtext>')
args = parser.parse_args()

def main(filename):
	file_list = [found_file for found_file in glob.glob(f'./**/*{file_name}', recursive=True)] # replaced '/home/jkligel/python_programs/**/*{filename} with current directory to look through.'
	for i in file_list:
		print(i)
	return file_list

def search(file_list, relatedtext):
	for file in file_list:
		if os.path.isfile(file):
			with open(file) as fr:
				for line in fr:
					if relatedtext in line:
						print(line)

if len(sys.argv) < 2:
	file_name = str(input('What file are you looking for? '))
	file_list = main(file_name)
	print()
	boolean = str(input('Do you want to search a file?(y/n)' ))
	if boolean == 'y':
		relatedtext = str(input('What is the text you are looking for? '))
		search(file_list[0], relatedtext)
else:
	file_name = args.file
	file_list = main(file_name)
	print()
	if args.search:
		search(file_list, args.search)
