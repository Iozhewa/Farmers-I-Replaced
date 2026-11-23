from setups import *
from movement import *
from maze_pack import place_hat
from poly import *

quota = 10**5
plant = Entities.Grass
def work_poly():
	lane = get_world_size() / 2
	
	place_hat()
	while num_drones() != max_drones():
		continue
	if num_items(itemOf(plant)) >= quota:
		return
	pos = (get_pos_x(), get_pos_y())
	for x in range(lane):
		for y in range(get_world_size()):
			visit(pos[0]+x, pos[1]+y)
			if num_items(itemOf(plant)) >= quota:
				return
			polyplant(plant)
			companion, spot = get_companion()
			if companion != None:
				visit(spot[0], spot[1])
				polyplant(companion)
				visit(pos[0]+x, pos[1]+y)
		goto(pos[0]+x, pos[1])
		column_collect()

def host_poly(goal=10**6, selection = Entities.Grass):
	global quota
	global plant
	quota = goal
	plant = selection

	quart = get_world_size() / 4
	for i in range(4):
		goto(quart*i, 0)
		plow()
		spawn_drone(work_poly)
	place_hat()
	work_poly()
