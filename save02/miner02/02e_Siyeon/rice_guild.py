from setups import *
from movement import *
from drone_pack import *
from rice import *

mid = get_world_size() / 2
bounds = (0, mid)

def work_rice():
	place_hat()
	while num_drones() != max_drones():
		continue
	
	pos = (get_pos_x(), get_pos_y())
	bounded_cycle(clayDig, pos)
	while get_ground_type() != Grounds.Rock:
		bounded_cycle(rice, pos)
		dig()
	bounded_cycle(collect, pos)

def host_rice():
	place_hat()
	for x in bounds:
		for y in bounds:
			goto(x, y)
			plow()
			spawn_drone(work_rice)
	work_rice()

if __name__ == "__main__":
	cycle(harvest)
	do_a_flip()
	clear()
	goto()
	host_rice()