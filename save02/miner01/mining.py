from movement import *
from setups import *

def powerset_2(a, b):
	result = []
	for x in (a, b):
		for y in (a, b):
			spot = (x, y)
			result.append(spot)
	return result

def dig_block():
	delta_coal = num_items(Items.Coal)
	while delta_coal > 0:
		for i in range(1, 8):
			corner_set = powerset_2(i, get_world_size()-1-i)
			for coord in corner_set:
				goto(coord[0], coord[1])
				for _ in range(0, 3):
					dig()
		delta_coal -= num_items(Items.Coal)

def dig_coal():
	found_clay = False
	while not(found_clay):
		for i in range(1, 8):
			corner_set = powerset_2(i, get_world_size()-1-i)
			for coord in corner_set:
				goto(coord[0], coord[1])
				for _ in range(0, 3):
					dig()
					found_clay = get_ground_type() == Grounds.Clay
			cycle(coal)

def farm_rice():
	found_rock = False
	while not(found_rock):
		found_rock = cycle(terrace)