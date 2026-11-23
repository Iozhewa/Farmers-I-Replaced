from setups import *
from movement import *

def display():
	while num_drones() != max_drones():
		continue
	do_a_flip()

def showcase():
	clear()
	for x in bounds:
		for y in bounds:
			goto(x, y)
			plow()
			spawn_drone(display)
	do_a_flip()
	
def place_hat():
	id = max_drones()
	id -= max_drones() - num_drones()
	if id == 1:
		change_hat(Hats.Gray_Hat)
	if id == 2:
		change_hat(Hats.Green_Hat)
	if id == 3:
		change_hat(Hats.Purple_Hat)
	if id == 4:
		change_hat(Hats.Brown_Hat)
		