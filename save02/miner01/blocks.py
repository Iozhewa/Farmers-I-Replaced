from movement import *
from setups import *

def powerset_2(a, b):
	result = []
	for x in (a, b):
		for y in (a, b):
			spot = (x, y)
			result.append(spot)
	return result

do_a_flip()

while num_items(Items.Block) < 50:
	goto()
	clear()
	for i in range(1, 8):
		corner_set = powerset_2(i, get_world_size()-i)
		for coord in corner_set:
			goto(coord[0], coord[1])
			for _ in range(0, 3):
				dig()

pet_the_piggy()