import atexit
import time

@atexit.register
def end_func():
	print('> END <\n')

def on_start():
	from utils.spread import spread_beasts
	from utils.visualization import visualizate
	from utils.prepare_data import prepare_data

	print('\n> START <')

	params = prepare_data()
	start_time = time.time()
	beasts = spread_beasts(*params)

	print("--- %s seconds ---" % (time.time() - start_time))

	visualizate(beasts)

if __name__ == '__main__':
	on_start()
