import pandas as pd
import csv

def csv_reader():
    pass
	# with open('employee_birthday.txt') as csv_file:
	# 	csv_reader = csv.reader(csv_file, delimiter=',')
	# 	line_count = 0
	# 	for row in csv_reader:
	# 		if line_count == 0:
	# 			print(f'Column names are {", ".join(row)}')
	# 			line_count += 1
	# 		else:
	# 			print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
	# 			line_count += 1
	# 	print(f'Processed {line_count} lines.')

	# with open('employee_birthday.txt', mode='r') as csv_file:
	# 	csv_reader = csv.DictReader(csv_file)
	# 	line_count = 0
	# 	for row in csv_reader:
	# 		if line_count == 0:
	# 			print(f'Column names are {", ".join(row)}')
	# 			line_count += 1
	# 		print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
	# 		line_count += 1
	# 	print(f'Processed {line_count} lines.')

# def
# data = pd.read_csv("tips.csv")
# display(data.head(10))

def visualizate(data):
	csv_reader()
	print('live ' + "{:_.0f}".format(len(data[0][0]) + len(data[0][1])))
	print('Death ' + "{:_.0f}".format(len(data[1][0]) + len(data[1][1])))
