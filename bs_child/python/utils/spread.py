def spread_beasts(min_live_time, live_time, start_count, years, min_children_count, children_count):
		# import time
		# from random import randrange, random
		# import string
		# import uuid
		# uuid.uuid4()
		# os.urandom(n)
		import random, string

		time = 2023
		beasts = [[[],[]],[[],[]]]

		def randomword(length):
			letters = string.ascii_lowercase
			return ''.join(random.choice(letters) for i in range(length))

		index = 0
		start_count = start_count / 2
		while index < start_count:
			beasts[0][0].append({
				'id': len(beasts[0][0]),
				'id_0': None,
				'id_1': None,
				'birthday': time,
				'gen': randomword(6) + ' ' + randomword(6)
			})
			beasts[0][1].append({
				'id': len(beasts[0][1]),
				'id_0': None,
				'id_1': None,
				'birthday': time,
				'gen': randomword(6) + ' ' + randomword(6)
			})
			index += 1

		# for index, element in enumerate(beasts):
		for count in range(years):
			time += count
			random.shuffle(beasts[0][0])
			for beast0, beast1 in zip(beasts[0][0], beasts[0][1]):
				current_children_count = random.randint(min_children_count, children_count)
				for count in range(current_children_count):
					list_number = random.randint(0, 1)
					# gen = ''
					# if list_number == 0:
						# beast0['gen'].split(" ")[0] + ' ' + beast1['gen'].split(" ")[1]
					# else:
						# beast1['gen'].split(" ")[1] + ' ' + beast0['gen'].split(" ")[0]

					beasts[0][list_number].append({
						'id': len(beasts[0][list_number]),
						'id_0': beast0['id'],
						'id_1': beast1['id'],
						'birthday': time,
						# 'gen': gen
						'gen': beast0['gen'].split(" ")[0] + ' ' + beast1['gen'].split(" ")[1]
					})

				if beast0['birthday'] + random.randint(min_live_time, live_time) < time:
					beasts[1][0].append(beast0)
					del beast0
				if beast1['birthday'] + random.randint(min_live_time, live_time) < time:
					beasts[1][1].append(beast1)
					del beast1

		return beasts
