#######################
# Author: Lori Oliver #
#					  #
# Convert Case 		  #
#######################

#!/usr/local/bin/python

import argparse, stringcase

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--camel", nargs='+', help="convert text to camel case: fooBarBoo")
parser.add_argument("-s", "--snake", nargs='+', help="convert text to snake case: foo_bar_boo")
parser.add_argument("-f", "--filename", nargs='+', help="convert file to a specified type default is camelcase")
parser.add_argument("-a", "--caps", nargs='+', help="convert to all caps")
parser.add_argument("-l", "--lower", nargs='+', help="convert to lower case")
parser.add_argument("-p", "--pascal", nargs='+', help="convert to pascal: FooBarBoo")
parser.add_argument("-d", "--path", nargs='+', help="convert to path case: foo/bar/boo")
parser.add_argument("-m", "--minus", nargs='+', help="convert to spinal case: foo-bar-boo")
args = parser.parse_args()

num = 0

# Convert to Camel Case
# CamelCase Caveats, _1 (underscore number) fails to convert
def camelCase(value):
	for value in args.camel:
		if value is not None:
			print "Camel: ", stringcase.camelcase(value)

# Convert to Snake Case
#print("Snakes: ", args.snake)
#print("S_Length: ", len(args.snake))
def snakeCase(value):
	for value in args.snake:
		if value is not None:
			print "Snake: ", stringcase.camelcase(value)
# Convert to All Caps
def allCaps(value):
	for value in args.caps:
		if value is not None:
			print "All Caps: ", stringcase.uppercase(value)
# Convert to Lower Case
def lowerCaps(value):
	for value in args.lower:
		if value is not None:
			print "Lower: ", stringcase.lowercase(value)
# Convert to Pascal Case
def pascalCase(value):
	for value in args.pascal:
		if value is not None:
			print "Pascal: ", stringcase.pascalcase(value)
# Convert to Path Case
def pathCase(value):
	for value in args.path:
		if value is not None:
			print "Path: ", stringcase.pathcase(value)
# Convert to Spinal Case
def spinalCase(value):
	for value in args.minus:
		if value is not None:
			print "Spinal: ", stringcase.spinalcase(value)
# Read from file write conversion to new/existing file
def convertFile(file, convertType = 'c'):
	readFile = ''
	if len(file) > 1:
		readFile = file[0].strip()
		convertType = file[1].strip()
	else:
		readFile = file[0].strip()
	if readFile[-3:] == 'txt':
		outfile = readFile.strip('.txt') + "_out.txt"
		print outfile
		o = open(outfile, "w+")
		f = open(readFile, "r")
		f1 = f.readlines()
		for line in f1:
			if convertType == 's':
				o.write(stringcase.snakecase(line).strip('_') + '\n')
			elif convertType == 'a':
				o.write(stringcase.uppercase(line))
			elif convertType == 'l':
				o.write(stringcase.lowercase(line))
			elif convertType == 'p':
				o.write(stringcase.pascalcase(line))
			elif convertType == 'd':
				o.write(stringcase.pathcase(line).strip('/') + '\n')
			elif convertType == 'm':
				o.write(stringcase.spinalcase(line).strip('-') + '\n')
			else:
				o.write(stringcase.camelcase(stringcase.lowercase(line)))
		f.close()
		o.close()
	else:
		print 'You will need to you use a .txt'

if(args.camel is not None):
	camelCase(args.camel)
if(args.snake is not None):
	snakeCase(args.snake)
if(args.caps is not None):
	allCaps(args.caps)
if(args.lower is not None):
	lowerCaps(args.lower)
if(args.pascal is not None):
	pascalCase(args.pascal)
if(args.path is not None):
	pathCase(args.path)
if(args.minus is not None):
	spinalCase(args.minus)

if(args.filename is not None):
	print "args.filename: ", args.filename
	print "lenth: ", len(args.filename)
	convertFile(args.filename)