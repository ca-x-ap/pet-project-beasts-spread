import random, string # import uuid # uuid.uuid4() # os.urandom(n)

def getStartBeasts(start_count, time):
	def randomword(length):
		letters = string.ascii_lowercase
		return ''.join(random.choice(letters) for i in range(length))

	def gen():
		return randomword(random.randint(3, 8)) + ' ' +randomword(random.randint(3, 8))

	beastsLive0 = []
	beastsLive1 = []

	for _ in range(int(start_count / 2)):
		beastsLive0.append({
			'id': len(beastsLive0),
			'id_0': None,
			'id_1': None,
			'birthday': time,
			'gen': gen()
		})
		beastsLive1.append({
			'id': len(beastsLive1),
			'id_0': None,
			'id_1': None,
			'birthday': time,
			'gen': gen()
		})

	return (beastsLive0, beastsLive1)

def beastes(beastsLive0, beastsLive1, time, min_children_count, children_count, min_live_time, live_time): # TODO rename me
	childrens0 = []
	childrens1 = []
	death0 = []
	death1 = []
	for beast0, beast1 in zip(beastsLive0, beastsLive1):
		current_children_count = random.randint(min_children_count, children_count)
		for count in range(current_children_count):
			if random.randint(0, 1) == 0:
				childrens0.append({
					'id': len(beastsLive0) + len(childrens0),
					'id_0': beast0['id'],
					'id_1': beast1['id'],
					'birthday': time,
					# 'gen': beast0['gen'].split(" ")[0] + ' ' + beast1['gen'].split(" ")[1]
				})
			else:
				childrens1.append({
					'id': len(beastsLive0) + len(childrens1),
					'id_0': beast0['id'],
					'id_1': beast1['id'],
					'birthday': time,
					# 'gen': beast0['gen'].split(" ")[0] + ' ' + beast1['gen'].split(" ")[1]
				})
		if beast0['birthday'] + random.randint(min_live_time, live_time) < time:
			death0.append(beast0)
			del beast0
		if beast1['birthday'] + random.randint(min_live_time, live_time) < time:
			death1.append(beast1)
			del beast1
	return (childrens0, childrens1, death0, death1)

def spread_beasts(min_live_time, live_time, start_count, years, min_children_count, children_count):
		time = 2023
		(beastsLive0, beastsLive1) = getStartBeasts(start_count, time)
		beastsDeath0 = []
		beastsDeath1 = []

		for count in range(years): # for index, element in enumerate(beasts):
			time += count
			random.shuffle(beastsLive0)

			(childrens0, childrens1, death0, death1) = beastes(beastsLive0, beastsLive1, time, min_children_count, children_count, min_live_time, live_time)

			beastsLive0.extend(childrens0)
			beastsLive1.extend(childrens1)
			beastsDeath0.extend(death0)
			beastsDeath1.extend(death1)

		return (beastsLive0, beastsLive1, beastsDeath0, beastsDeath1)
