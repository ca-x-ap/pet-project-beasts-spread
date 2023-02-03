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

def visualizate(beastsLive0, beastsLive1, beastsDeath0, beastsDeath1):
	live = "{:_.0f}".format(len(beastsLive0) + len(beastsLive1))
	death = "{:_.0f}".format(len(beastsDeath0) + len(beastsDeath1))
	both = "{:_.0f}".format((len(beastsDeath0) + len(beastsDeath1)) - (len(beastsLive0) + len(beastsLive1)))

	beasts0 = "{:_.0f}".format(len(beastsLive0))
	beastsDeath0 = "{:_.0f}".format(len(beastsDeath0))
	beastsBoth0 = "{:_.0f}".format(len(beastsDeath0) - len(beastsLive0))

	beasts1 = "{:_.0f}".format(len(beastsLive1))
	beastsDeath1 = "{:_.0f}".format(len(beastsDeath1))
	beastsBoth1 = "{:_.0f}".format(len(beastsDeath1) - len(beastsLive1))

	print(f"""
		Total:    { live } | { death } | { both }
		beasts#0: { beasts0 } | { beastsDeath0 } | { beastsBoth0 }
		beasts#1: { beasts1 } | { beastsDeath1 } | { beastsBoth1 }
		""")
	# print('live ' + )
	# print('Death ' + )

	csv_reader()
