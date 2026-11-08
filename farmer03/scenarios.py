from helpers import *

def collect():
	dead = get_entity_type() == Entities.Dead_Pumpkin
	if can_harvest() or dead:
		harvest()	

def plow(ground=Grounds.Soil):
	collect()
	if get_ground_type() != ground:
		till()

def hay():
	collect()
	if get_ground_type() != Grounds.Grassland:
		till()

def carrots(buds=False):
	step = 3
	align = "y"
	if reserved(step, align) and buds:
		plow()
		plant(Entities.Sunflower)
	elif reserved(step, align):
		plow(Grounds.Grassland)  # Looks nicer
		plant(Entities.Bush)
	else:
		plow()
		plant(Entities.Carrot)
	water()

def trees(buds=False):
	step = 2
	align = "_"
	if reserved(step, align) and buds:
		plow()
		plant(Entities.Sunflower)
	elif reserved(step, align):
		plow(Grounds.Grassland)
		plant(Entities.Bush)
	else:
		plow(Grounds.Grassland)
		plant(Entities.Tree)
	water()

def pumpkins(buds=False):
	step = 4
	align = "x"
	if reserved(step, align) and buds:
		plow()
		plant(Entities.Sunflower)
	elif reserved(step, align):
		plow(Grounds.Grassland)
		plant(Entities.Bush)
	else:
		corner_x = {2, 5, 8, 11}
		corner_y = {1, 5, 9}
		x, y = (get_pos_x(), get_pos_y())
	
		corner_pos = x in corner_x and y in corner_y
		entity = get_entity_type()
		if entity == Entities.Pumpkin and corner_pos:
			collect()
		elif entity == Entities.Pumpkin:
			return
		else:
			plow()
			plant(Entities.Pumpkin)
	water()

def coal(charging=False):
	if get_ground_type() == Grounds.Coal:
		dig()
	elif charging:
		plow()
		if ((random() * 10) // 1) % 3 == 0:
			plant(Entities.Carrot)
		else:
			plant(Entities.Sunflower)
	else:
		collect()

def rice(charging=False):
	ground = get_ground_type()
	collect()
	if ground == Grounds.Clay:
		plant(Entities.Rice)
	elif ground == Grounds.Dirt and charging:
		plow()
		plant(Entities.Sunflower)
	elif ground == Grounds.Rock:
		return
	else:
		dig()

def weird():
	pass

def cactus():
	pass
