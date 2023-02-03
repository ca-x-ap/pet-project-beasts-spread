def spread_beasts(min_live_time, live_time, start_count, years, min_children_count, children_count):
		import random, string # import uuid # uuid.uuid4() # os.urandom(n)

		time = 2023
		# beasts = [[[],[]],[[],[]]]
		beastsLive0 = []
		beastsLive1 = []
		beastsDeath0 = []
		beastsDeath1 = []

		def randomword(length):
			letters = string.ascii_lowercase
			return ''.join(random.choice(letters) for i in range(length))

		for _ in range(int(start_count / 2)):
			beastsLive0.append({
				'id': len(beastsLive0),
				'id_0': None,
				'id_1': None,
				'birthday': time,
				'gen': randomword(2) + ' ' + randomword(2)
			})
			beastsLive1.append({
				'id': len(beastsLive1),
				'id_0': None,
				'id_1': None,
				'birthday': time,
				'gen': randomword(2) + ' ' + randomword(2)
			})

		for count in range(years): # for index, element in enumerate(beasts):
			time += count
			random.shuffle(beastsLive0)
			# childrens0 = []
			# childrens1 = []
			# death0 = []
			# death1 = []

			for beast0, beast1 in zip(beastsLive0, beastsLive1):
				current_children_count = random.randint(min_children_count, children_count)
				for count in range(current_children_count):
					if random.randint(0, 1) == 0:
						beastsLive0.append({
							'id': len(beastsLive0) + len(beastsLive0),
							'id_0': beast0['id'],
							'id_1': beast1['id'],
							'birthday': time,
							'gen': beast0['gen'].split(" ")[0] + ' ' + beast1['gen'].split(" ")[1]
						})
					else:
						beastsLive1.append({
							'id': len(beastsLive0) + len(beastsLive1),
							'id_0': beast0['id'],
							'id_1': beast1['id'],
							'birthday': time,
							'gen': beast0['gen'].split(" ")[0] + ' ' + beast1['gen'].split(" ")[1]
						})
				if beast0['birthday'] + random.randint(min_live_time, live_time) < time:
					beastsDeath0.append(beast0)
					del beast0
				if beast1['birthday'] + random.randint(min_live_time, live_time) < time:
					beastsDeath0.append(beast1)
					del beast1

			# beastsLive0.extend(childrens0)
			# beastsLive1.extend(childrens1)
			# beastsDeath0.extend(death0)
			# beastsDeath1.extend(death1)

		return (beastsLive0, beastsLive1, beastsDeath0, beastsDeath1)
