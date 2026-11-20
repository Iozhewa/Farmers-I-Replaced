def simple():
	return

def collect():
	dead = get_entity_type == Entities.Dead_Pumpkin
	if can_harvest() or dead:
		harvest()

def plow(preferred=Grounds.Soil):
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
	else:  # Implicitly carrot
		plow(Grounds.Soil)
		plant(Entities.Carrot)
		water()

def cycle(request=simple):
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			move(East)
			request()
		move(North)
		