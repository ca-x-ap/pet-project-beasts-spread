import atexit
import sys
import time

@atexit.register
def end_func():
	print('> END <\n')

def on_startup():
	from utils.spread import spread_beasts
	from utils.visualization import visualizate

	# for x in fruits:
	#   print(x)
	# print(beasts)
	# print(beasts.live)
	# print(beasts.death)
	# print(beasts.live[0])
	# print(beasts.live[1])

	years = 0
	min_live_time = 0
	live_time = 3
	start_count = 20
	min_children_count = 0
	children_count = 3

	len_sys_argv = len(sys.argv) - 1

	print(f'Starting { sys.argv[0] }')
	if len_sys_argv == 0 or len_sys_argv == 1:
		print('Need wrinte next arguments:')
		print('(You can run app as "app.py years_count(0)(need write) start_count(20) children_count(3) min_children_count(0) live_time(3) min_live_time(0)" )')

	if len_sys_argv >= 1:
		years = int(sys.argv[1])
	else:
		years = int(input('Years count (can be esasd): '))

	if len_sys_argv >= 2:
		start_count = int(sys.argv[2])

	if len_sys_argv >= 3:
		children_count = int(sys.argv[3])

	if len_sys_argv >= 4:
		min_children_count = int(sys.argv[4])

	if len_sys_argv >= 5:
		live_time = int(sys.argv[5])

	if len_sys_argv >= 6:
		min_live_time = int(sys.argv[6])

	print(f"""
		years_count: { years }
		start_count: { start_count }
		children_count: { children_count }
		min_children_count: { min_children_count }
		live_time: { live_time }
		min_live_time: { min_live_time }
		""")

	start_time = time.time()
	beasts = spread_beasts(min_live_time, live_time, start_count, years, min_children_count, children_count)
	print("--- %s seconds ---" % (time.time() - start_time))
	visualizate(beasts)

if __name__ == '__main__':
	print('\n> START <')
	on_startup()
