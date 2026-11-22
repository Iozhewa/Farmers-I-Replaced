from setups import *
from movement import *

heights = []
for i in range(get_world_size()):
	heights.append(i)

def plant_bamboo():
	goto()
	for i in range(get_world_size()):
		move(North)
		plow()
		plant(Entities.Bamboo)
		heights[i] = measure()
	move(East)

def watch_bamboo():
	start = get_time()
	elapsed = get_time() - start
	while elapsed < max(heights):
		for _ in range(get_world_size()):
			move(North)
			collect()
			plow()
			plant(Entities.Carrot)
			water()
		elapsed = get_time() - start

def trim_bamboo():
	goto(1, 0)
	for i in range(len(heights)):
		move(North)
		hover(heights[i])
		move(West)
		heights[i] = measure()
		move(East)
	goto(1, 0)

def reset_bamboo():
	endpoint = get_world_size() - 1
	goto(1, endpoint)
	hover(0)
	goto(0, endpoint)
	goto()

def farm_bamboo():
	change_hat(Hats.Bamboo_Hat)
	#global heights
	#heights = []
	plant_bamboo()
	while max(heights) < 11:
		watch_bamboo()
		trim_bamboo()
	reset_bamboo()
	