from setups import *
from movement import *
from drone_pack import place_hat
# from bamboo import *

height = 19
def work_bamboo():
	place_hat()
	while num_drones() != max_drones():
		continue
	for i in range(get_world_size()):
		move(North)
		plow()
		plant(Entities.Bamboo)
		global height
		if get_entity_type(North) == Entities.Bamboo:
			height = min(measure(), measure(North))
		else:
			height = min(height, measure())
	move(East)
	while height < 7:  # TODO: Fix breakpoint if 5 fails
		watch_bamboo()
		trim_bamboo()
	reset_bamboo()

def watch_bamboo():
	start = get_time()
	elapsed = get_time() - start
	while elapsed < height:
		for _ in range(get_world_size()):
			move(North)
			collect()
			plow()
			plant(Entities.Carrot)
			water()
		elapsed = get_time() - start

def trim_bamboo():
	pos = (get_pos_x(), get_pos_y())
	goto(pos[0], pos[1])
	for i in range(get_world_size()):
		move(North)
		hover(height)
		move(West)
		global height
		if get_entity_type(North) != None:
			height = min(measure(), measure(North))
		else:
			height = min(height, measure())
		move(East)
	goto(pos[0], pos[1])

def reset_bamboo():
	endpoint = get_world_size() - 1
	pos = (get_pos_x(), get_pos_y())
	goto(pos[0], endpoint)
	hover(0)
	goto(pos[0]-1, endpoint)
	goto(pos[0]-1, pos[1])
	
	goto(pos[0], pos[1])
	for _ in range(get_world_size()):
		move(North)
		if can_harvest():
			harvest()
		
def host_bamboo():
	quart = get_world_size() / 4
	place_hat()
	for i in range(4):
		goto(quart*i, 0)
		plow()
		spawn_drone(work_bamboo)
	work_bamboo()
