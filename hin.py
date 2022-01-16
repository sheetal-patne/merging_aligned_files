import os
import time
import re

def stringSplitByNumbers(x):
    r = re.compile('(\\d+)')
    l = r.split(x)
    return [int(y) if y.isdigit() else y for y in l]

def main():
	fname = []
	path = './' + str(raw_input("Enter the name of the directory (Hindi files): "))
	
	if not os.path.exists(path):
		print("There is no directory with the name entered by you.")
		exit()

	else:
		print("There are no files in the directory name entered by you.")
		exit()

	for dirpath, dirs, files in os.walk(path):	
		for filename in files:
			fname.append(os.path.join(dirpath,filename))

	fname = sorted(fname, key = stringSplitByNumbers)
	fout = open("output_hindi", 'a')

	for file in fname:
		print("Extracting text from " + file)

		with open(file) as fin:
			fout.write(fin.read())

		fin.close()
	
	fout.close()
	print("\nThe aligned files were combined into a text file named \'output_hindi\'")

if __name__ == '__main__':
	main()