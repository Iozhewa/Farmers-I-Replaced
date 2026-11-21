def simple():
	return

def collect():
	dead = get_entity_type == Entities.Dead_Pumpkin
	if can_harvest() or dead:
		harvest()

def plow(preferred=Grounds.Soil, strict=False):
	if not(strict):
		collect()
	if get_ground_type() != preferred:
		till()

def deplow():
	plow(Grounds.Grassland)

def water(preferred=0.5):
	if get_water() < preferred:
		use_item(Items.Water)

def polyplant(partner=Entities.Grass):
	if partner == Entities.Grass:
		plow(Grounds.Grassland)
	elif partner == Entities.Bush:
		plow(Grounds.Grassland)
		plant(Entities.Bush)
	elif partner == Entities.Tree:
		plow(Grounds.Grassland)
		plant(Entities.Tree)
	elif partner == Entities.Sunflower:  # refactor
		plow(Grounds.Soil)
		plant(Entities.Sunflower)
		water()
	elif partner == Entities.Pumpkin:
		plow(Grounds.Soil, True)
		plant(Entities.Pumpkin)
		water(0.2)
	else:  # Implicitly carrot
		plow(Grounds.Soil)
		plant(Entities.Carrot)
		water()

def pluck(petals=11):
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			move(East)
			if measure() == petals:
				harvest()
		move(North)

def column_collect():
	for _ in range(get_world_size()):
		move(North)
		collect()

def terrace():
	acceptable = Grounds.Dirt, Grounds.Dry_Rice_Terrace, Grounds.Coal
	collect()
	while get_ground_type() in acceptable:
		dig()
	if get_ground_type() == Grounds.Clay:
		plant(Entities.Rice)

def cycle(request=simple):
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			move(East)
			request()
		move(North)
		