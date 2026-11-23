from setups import *
from movement import *
from maze_pack import place_hat

mid = get_world_size() / 2
bounds = (0, mid)

quota = 200
def work_sunflower():
	place_hat()
	while num_drones() != max_drones():
		continue
	while num_items(Items.Power) < quota:
		if num_items(Items.Carrot) < 1:
			print("Exhausted input!")
			return
			
		petals = set()
		lane = get_world_size() / 2
		pos = (get_pos_x(), get_pos_y())
		for x in range(lane):
			for y in range(lane):
				goto(pos[0]+x, pos[1]+y)
				polyplant(Entities.Sunflower)
				petals.add(measure())
				
		while len(petals) > 0:
			most = max(petals)
			for x in range(lane):
				for y in range(lane):
					goto(pos[0]+x, pos[1]+y)
					if measure() == most:
						harvest()
					
			petals.remove(most)
		goto(pos[0], pos[1])
	
def host_sunflower(goal=200):
	global quota
	quota = goal
	for x in bounds:
		for y in bounds:
			goto(x, y)
			plow()
			spawn_drone(work_sunflower)
	place_hat()
	work_sunflower()