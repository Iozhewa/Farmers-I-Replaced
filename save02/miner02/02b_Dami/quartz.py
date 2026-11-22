from movement import *
from setups import *

def quartz():
	if get_ground_type() == Grounds.Quartz:
		dig()

mid = get_world_size()/2
def farm_quartz(quota=60):
	change_hat(Hats.Wizard_Hat)
	goto(mid, mid)
	while num_items(Items.Quartz) < quota:
		if num_items(Items.Iron) < 1:
			print("Exhausted input!")
			return
		prospect = prospect_quartz()
		while prospect == None:
			for _ in range(5):
				dig()
			prospect = prospect_quartz()
		while prospect >= 2:
			for _ in range(2):
				dig()
			prospect = prospect_quartz()
			
		z = get_pos_z()
		goto()
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				move(North)
				while get_pos_z() > z:
					dig()
				while get_ground_type() == Grounds.Quartz:
					dig()
			move(East)