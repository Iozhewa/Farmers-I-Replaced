from setups import *
from movement import *
from drone_pack import *
from iron import *

quota = 400
def work_iron():
	pos = (get_pos_x(), get_pos_y())
	place_hat()
	while num_items(Items.Iron) < quota:
		if num_items(Items.Coal) < 1:
			print("Exhausted input!")
			return
		prospect = prospect_iron()
		while prospect != None:
			move(prospect)
			prospect = prospect_iron()
		counter = 0
		while get_ground_type() == Grounds.Iron or counter < 5:
			dig()
			counter += 1
		

def host_iron(goal=400):
	global quota
	quota = goal
	
	quart = get_world_size() / 4
	place_hat()
	for i in range(4):
		goto(0, quart*i)
		plow()
		spawn_drone(work_iron)
	work_iron()