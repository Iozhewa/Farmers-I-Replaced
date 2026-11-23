from setups import *
from movement import *
from maze_pack import *
from pumpkins import *

mid = get_world_size() / 2
bounds = (0, mid)

quota = 10**5
def work_pumpkin():
	place_hat()
	while num_drones() != max_drones():
		continue
	while num_items(Items.Pumpkin) < quota:
		if num_items(Items.Carrot) < 1:
			print("Exhausted input!")
			return
		
		lane = get_world_size() / 2
		pos = (get_pos_x(), get_pos_y())
		for x in range(lane):
			for y in range(lane):
				goto(pos[0]+x, pos[1]+y)
				spot = (get_pos_x(), get_pos_y())
				if should_harvest(spot, (pos[0], pos[0]+lane)):
					harvest()
				polyplant(Entities.Pumpkin)
		goto(pos[0], pos[1])

def host_pumpkin(goal=10**5):
	global quota
	quota = goal
	for x in bounds:
		for y in bounds:
			goto(x, y)
			plow()
			spawn_drone(work_pumpkin)
	place_hat()
	work_pumpkin()
	