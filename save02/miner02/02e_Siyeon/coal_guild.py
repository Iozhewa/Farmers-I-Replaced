from setups import *
from movement import *
from drone_pack import *
from coal import *

def work_coal():
	pos = (get_pos_x(), get_pos_y())
	place_hat()
	while True:
		for x in range(get_world_size()-1):
			if x % 2 == 0:
				goto(x+pos[0], pos[1])
			else:
				goto(x+pos[0], pos[1]+2)
			for _ in range(2):
				if get_ground_type() == Grounds.Coal:
					for _ in range(get_world_size()):
						coal()
						move(East)
				if get_stability() > 2:
					return
				dig()

def host_coal():
	quart = get_world_size() / 4
	place_hat()
	for i in range(4):
		goto(0, quart*i)
		plow()
		spawn_drone(work_coal)
	work_coal()