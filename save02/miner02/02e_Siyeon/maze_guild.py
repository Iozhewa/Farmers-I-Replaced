from setups import *
from movement import *
from maze_pack import place_hat
from mazes import *
from solutions import *

bounds = (3, 12)
# (5, 10), (4, 11), (3, 12)

quota = 6000
def work_maze():
	place_hat()
	while num_drones() != max_drones():
		continue
	
	limit = 6
	farm_treasure(quota, limit)
	harvest()
	print("Met quota!")

def host_maze(goal=6000):
	global quota
	quota = goal
	for x in bounds:
		for y in bounds:
			goto(x, y)
			plow()
			spawn_drone(work_maze)
	work_maze()

mid = get_world_size() / 2
def guild_setup(size=num_drones()):
	goto(mid, mid)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, size)

def guild_maze(quota=2.6*10**5, limit=get_world_size()):
	counter = 4
	while num_items(Items.Gold) < quota:
		collect()
		goto(mid, mid)
		setup(counter)
		if counter == 1:
			trivial_solution()
		else:
			right_hand_agents()
			place_hat()
		if counter == limit:
			counter = 1
		else:
			counter += 1