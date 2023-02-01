import atexit
import sys

@atexit.register
def end_func():
	print('> END <\n')

def on_startup():
	from utils.spread import spread_beasts

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

	len_sys_argv = len(sys.argv) - 1
	print(f'Starting { sys.argv[0] }')
	if len_sys_argv == 0 or len_sys_argv == 1:
		print('Need wrinte next arguments:')
		print('(You can run app as "app.py years_count(0)(need write) start_count(20) live_time(3) min_live_time(0)" )')

	if len_sys_argv >= 1:
		years = int(sys.argv[1])
	else:
		years = int(input('Years count (can be esasd): '))

	if len_sys_argv >= 2:
		start_count = int(sys.argv[2])

	if len_sys_argv >= 3:
		live_time = int(sys.argv[3])

	if len_sys_argv >= 4:
		min_live_time = int(sys.argv[4])

	print(f"""
		years_count: { years }
		start_count: { start_count }
		live_time: { live_time }
		min_live_time: { min_live_time }
		""")

	beasts = spread_beasts(min_live_time, live_time, start_count, years)
	print('live ' + str(len(beasts[0][0])) + str(len(beasts[0][1])))
	print('death ' + str(len(beasts[1][0])) + str(len(beasts[1][1])))

if __name__ == '__main__':
	print('\n> START <')

	on_startup()
