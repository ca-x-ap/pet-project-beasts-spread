def spread_beasts():
		# import time
		# from random import randrange, random
		# import string
		# import uuid
		# uuid.uuid4()
		# os.urandom(n)
		import random, string

		time = 2023
		live_time = 3
		beasts = [[[],[]],[[],[]]]
		def randomword(length):
			letters = string.ascii_lowercase
			return ''.join(random.choice(letters) for i in range(length))
		index = 0
		while index < 20:
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
		for count in range(3):
			time += count
			random.shuffle(beasts[0][0])
			# random.shuffle(beasts[0][1])
			for beast0, beast1 in zip(beasts[0][0], beasts[0][1]):
				list_number = random.randint(0, 1)
				beasts[0][list_number].append({
					'id': len(beasts[0][list_number]),
					'id_0': beast0['id'],
					'id_1': beast1['id'],
					'birthday': time,
					'gen': beast0['gen'].split(" ")[0] + ' ' + beast1['gen'].split(" ")[1]
				})

				if beast0['birthday'] + random.randint(0, live_time) < time:
					beasts[1][0].append(beast0)
					del beast0
				if beast1['birthday'] + random.randint(0, live_time) < time:
					beasts[1][1].append(beast1)
					del beast1

		print('live ' + str(len(beasts[0][0])) + str(len(beasts[0][1])))
		print('death ' + str(len(beasts[1][0])) + str(len(beasts[1][1])))

		# for x in fruits:
		#   print(x)
		# print(beasts)
		# print(beasts.live)
		# print(beasts.death)
		# print(beasts.live[0])
		# print(beasts.live[1])
